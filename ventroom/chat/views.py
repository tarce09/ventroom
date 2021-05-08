from django.shortcuts import render
from .models import Message
# Create your views here.
def home(request):
    return render(request,'chat/home.html')

def index(request):
    return render(request,'chat/chat.html')

def room(request, room_name):
    username = request.GET.get('username','Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    
    return render(request,'chat/room.html',{'room_name':room_name,'username':username, 'messages':messages})