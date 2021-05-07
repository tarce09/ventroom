from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'chat/index.html')

def room(request, room_name):
    username = request.GET.get('username','Anonymous')
    
    return render(request,'chat/room.html',{'room_name':room_name,'username':username})