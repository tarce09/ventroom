from django.urls import path


from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('',views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]