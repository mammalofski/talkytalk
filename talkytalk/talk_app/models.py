from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    ROOM_STATUS = (
        (1, 'open'),
        (2, 'on_call'),
        (3, 'closed'),
    )
    callee = models.ForeignKey(User, related_name='rooms', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User)
    room_id = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=ROOM_STATUS, default=1)

    def __str__(self):
        return self.room_id


class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    contact = models.ForeignKey(User, related_name='reverse_contacts', on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=120)
    detail = models.CharField(max_length=240, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name
