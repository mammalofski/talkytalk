from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=120)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    content = models.CharField(max_length=240)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Sender : {} at Room: {}".format(self.sender, self.room)
