import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
from .prof import prof_filter
from .sentiment import fetch_sentiment
class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope ['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        #apply profanity filter to the message
        message = prof_filter(message)
        sentiment = fetch_sentiment(message)
        sentiment = str(sentiment)
        

        username = data['username']
        room = data['room']

        await self.save_message(username,room,message,sentiment)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username':username,
                

            }
        )


    async def chat_message(self, event):
        message = event['message']
        #apply profanity filter to message 
        sentiment = fetch_sentiment(message)
        message = prof_filter(message)

        sentiment = str(sentiment)
        print("SENTIMENT "+ sentiment)
        
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'sentiment':sentiment,
        }))



    @sync_to_async
    def save_message(self,username,room,message,sentiment):
        Message.objects.create(username=username,room=room,content=message,sentiment=sentiment)
