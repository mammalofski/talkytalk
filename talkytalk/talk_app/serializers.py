from rest_framework import serializers
from . import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'callee',
            'participants',
            'created',
            'status',
            'room_id',
        )
        model = models.Room
        validators = []  # remove default validation


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'owner',
            'contact',
            'contact_name',
            'detail',
            'created',
        )
        model = models.Contact

