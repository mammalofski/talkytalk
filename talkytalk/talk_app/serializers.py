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

    def create(self, validated_data):
        # create the room
        room = models.Room.objects.create(
            callee=self.context['request'].user,
            room_id=validated_data.get('room_id'),
        )
        # then add the callee himself/herself to participants
        room.participants.add(self.context['request'].user.id)
        return room


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

