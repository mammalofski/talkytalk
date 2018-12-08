from rest_framework import generics
from . import models
from . import serializers


class ListCreateRoom(generics.ListCreateAPIView):
    serializer_class = serializers.RoomSerializer

    def get_queryset(self):
        return models.Room.objects.filter(callee=self.request.user)
        # return models.Room.objects.all()


