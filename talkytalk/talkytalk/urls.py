"""talkytalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path
import django_eventstream
from django.views.generic import TemplateView
from rest_auth.registration.views import VerifyEmailView
from allauth.account.views import confirm_email
import talk_app.views as talkAppViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('userAuth/', TemplateView.as_view(template_name='auth.html')),
    path('contacts/', TemplateView.as_view(template_name='contacts.html')),
    path('rooms/', TemplateView.as_view(template_name='room.html')),
    path('chats/', TemplateView.as_view(template_name='chats.html')),
    path('admin/', admin.site.urls),
    path('api/', include(('talk_app.urls', 'talk_app'), namespace='talk_app')),
    path('events/', include(django_eventstream.urls), {'channels': ['testChannel']}),
    # REST AUTH
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path('account-confirm-email/', VerifyEmailView.as_view(),
            name='account_email_verification_sent'),
    re_path('rest-auth/registration/account-confirm-email/(?P<key>\w+)/', confirm_email,
            name="confirm_email"),
    re_path('account-confirm-email/(?P<key>\w+)/', confirm_email,
            name="confirm_email"),
    path('reset/(?int::<first_token>\w+)/(?int::<password_reset_token>[-\w]+)/', talkAppViews.confirm_password_reset,
         name="confirm_password_reset"),
]

urlpatterns += staticfiles_urlpatterns()
