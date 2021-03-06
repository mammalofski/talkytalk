from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password='1', username='', first_name='', last_name=''):
        if password != '1' and len(password) < 8:
            raise ValueError('password must have at least 8 character.')

        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email=self.normalize_email(email), first_name=first_name, last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_usable_password(self):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        app_label = 'talk_app'


class TalkyTalkUser(AbstractBaseUser):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=30, blank=True, null=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    def get_username(self):
        return self.username

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_usable_password(self):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        app_label = 'talk_app'


class Room(models.Model):
    ROOM_STATUS = (
        (1, 'open'),
        (2, 'on_call'),
        (3, 'closed'),
    )
    callee = models.ForeignKey(TalkyTalkUser, related_name='rooms', on_delete=models.CASCADE)
    participants = models.ManyToManyField(TalkyTalkUser, blank=True)
    room_id = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=ROOM_STATUS, default=1)

    def __str__(self):
        return self.room_id


class Contact(models.Model):
    owner = models.ForeignKey(TalkyTalkUser, related_name='contacts', on_delete=models.CASCADE)
    contact = models.ForeignKey(TalkyTalkUser, related_name='reverse_contacts', on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=120)
    detail = models.CharField(max_length=240, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name


class Message(models.Model):
    sender = models.ForeignKey(TalkyTalkUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(TalkyTalkUser, related_name='received_messages', on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


