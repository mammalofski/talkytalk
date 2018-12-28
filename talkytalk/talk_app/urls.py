from django.urls import path
from . import views

urlpatterns = [
    path('getUser/', views.GetUserDetails.as_view(), name='get_user_details'),
    path('room/', views.ListCreateRoom.as_view(), name='list_room'),
    path('room/<int:pk>', views.RetrieveUpdateDestroyRoom.as_view(), name='room_detail'),
    path('room/join', views.JoinRoom.as_view(), name='join_room'),
    path('contact', views.ListCreateContact.as_view(), name='list_contact'),
    path('contact/<int:pk>', views.RetrieveUpdateDestroyContact.as_view(), name='contact_detail'),
    path('message/', views.ListMessage.as_view(), name='list_message'),
]
