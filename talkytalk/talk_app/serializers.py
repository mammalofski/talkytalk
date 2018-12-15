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

    # def create(self, validated_data):
    #     print('in room creation')
    #     # create the room
    #     room = models.Room.objects.create(
    #         # callee=self.context['request'].user,
    #         callee=models.User.objects.get(id=1),  # TODO: replace this line later
    #         room_id=validated_data.get('room_id'),
    #     )
    #     # then add the callee himself/herself to participants
    #     # room.participants.add(self.context['request'].user.id)
    #     room.participants.add(1)  # TODO: replace this line later
    #     return room

    def validate(self, data):
        print('in room validator')
        room_id = data.get('room_id')
        if not (isinstance(room_id, str) and room_id):
            raise serializers.ValidationError("field room_id must be a non empty string")

        # if models.Room.objects.filter(room_id=room_id, owner=self.context['request'].user).exists():
        if models.Room.objects.filter(room_id=room_id).exists():  # TODO: replace this line later
            raise serializers.ValidationError("room with this ID is taken")

        return data


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

