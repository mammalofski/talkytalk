from rest_framework import serializers
from . import models

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'users',
        )
        model = models.Room


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'sender',
            'room',
            'content',
            'created'
        )
        model = models.Message
