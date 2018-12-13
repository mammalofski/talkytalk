from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


class ListCreateRoom(generics.ListCreateAPIView):
    serializer_class = serializers.RoomSerializer

    def get_queryset(self):
        return models.Room.objects.filter(callee=self.request.user)


class RetrieveUpdateDestroyRoom(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()

    def get_object(self):
        return get_object_or_404(self.queryset, id=self.kwargs.get('pk'), callee=self.request.user)


class JoinRoom(generics.CreateAPIView):
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()

    def create(self, request, *args, **kwargs):
        room = get_object_or_404(models.Room, room_id=request.data.get('room_id'))
        room.participants.add(request.user.id)
        serializer = self.serializer_class(room)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

