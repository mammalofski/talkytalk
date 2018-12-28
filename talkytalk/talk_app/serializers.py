from rest_framework import serializers
from . import models

from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import settings

from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists, get_username_max_length)
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from allauth.account.models import EmailAddress
from allauth.account.forms import ResetPasswordForm
from rest_auth.serializers import PasswordResetSerializer, PasswordResetConfirmSerializer, \
    PasswordChangeSerializer

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.serializers import UserDetailsSerializer

User = get_user_model()


class UserSerializer(UserDetailsSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        read_only_fields = ('email', 'id',)


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()


class PasswordSerializer(PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    def save(self):
        if not EmailAddress.objects.filter(user=self.user).exists():
            EmailAddress.objects.create(user=self.user, email=self.user.email, verified=True, primary=True)
        return self.set_password_form.save()


class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(
            settings, 'OLD_PASSWORD_FIELD_ENABLED', False
        )
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

        self.empty_old_password = True if self.user.password == '' else False

        if not self.old_password_field_enabled or self.empty_old_password:
            self.fields.pop('old_password')

    def save(self):
        super().save()
        if self.empty_old_password:
            if not EmailAddress.objects.filter(user=self.user).exists():
                EmailAddress.objects.create(user=self.user, email=self.user.email, verified=True, primary=True)


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


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'sender',
            'receiver',
            'message',
            'created',
        )
        model = models.Message
