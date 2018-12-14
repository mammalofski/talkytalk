from django.urls import path, include
from . import views

urlpatterns = [
    path('room/', views.ListCreateRoom.as_view(), name='list_room'),
    path('room/<int:pk>', views.RetrieveUpdateDestroyRoom.as_view(), name='room_detail'),
    path('room/join', views.JoinRoom.as_view(), name='join_room'),
    path('contact', views.ListCreateContact.as_view(), name='list_contact'),
    path('contact/<int:pk>', views.RetrieveUpdateDestroyContact.as_view(), name='contact_detail'),
]
