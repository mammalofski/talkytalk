from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  AllowAny

from . import models
from . import serializers


def confirm_password_reset(request, first_token, password_reset_token):
    return redirect("/auth/#/resetPasswordConfirm/" + first_token + "/" + password_reset_token)


def confirm_email(request, key):
    return redirect("/auth/#/verifyEmail/" + key)

class ListCreateRoom(generics.ListCreateAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = (AllowAny,)  # TODO: replace this line later

    def get_queryset(self):
        # return models.Room.objects.filter(callee=self.request.user)  # TODO: replace this line later
        return models.Room.objects.all()

    def create(self, request, *args, **kwargs):
        print('in room creation')

        # if models.Room.objects.filter(room_id=request.data.get('room_id'), callee=request.user).exists():  # TODO: replace this line later
        if models.Room.objects.filter(room_id=request.data.get('room_id')).exists():
            return Response('room with this id already exists', status=status.HTTP_406_NOT_ACCEPTABLE)

        # create the room
        room = models.Room.objects.create(
            # callee=self.context['request'].user,
            callee=models.User.objects.get(id=1),  # TODO: replace this line later
            room_id=request.data.get('room_id'),
        )
        # then add the callee himself/herself to participants
        # room.participants.add(self.context['request'].user.id)
        room.participants.add(1)  # TODO: replace this line later
        serializer = self.serializer_class(room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyRoom(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()

    def get_object(self):
        return get_object_or_404(self.queryset, id=self.kwargs.get('pk'), callee=self.request.user)


class JoinRoom(generics.CreateAPIView):
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()
    permission_classes = (AllowAny,)  # TODO: replace this line later

    def create(self, request, *args, **kwargs):
        # get the room
        room = get_object_or_404(models.Room, room_id=request.data.get('room_id'))
        # add user to room participants
        # room.participants.add(request.user.id)
        room.participants.add(2)  # TODO: replace this line later
        # change room status to "on_call"
        room.status = 2
        room.save()
        # serialize the data
        serializer = self.serializer_class(room)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ListCreateContact(generics.ListCreateAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        return models.Contact.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # save the contact with owner of the user
        serializer.save(owner=self.request.user)


class RetrieveUpdateDestroyContact(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()

    def get_object(self):
        return get_object_or_404(self.queryset, id=self.kwargs.get('pk'), owner=self.request.user)

