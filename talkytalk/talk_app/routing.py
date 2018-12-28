from django.conf.urls import url
from django.urls import path
from channels.routing import URLRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
import django_eventstream
from . import consumers

ws_urlpatterns = [
    # url(r'^chat/(?P<username>[^/]+)$', consumers.ChatConsumer),
    path('chat/<str:username>/', consumers.ChatConsumer),
]

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<username>[^/]+)/$', consumers.ChatConsumer),
    # url('ws/', AuthMiddlewareStack(
    #     URLRouter(ws_urlpatterns)
    # ), {'channels': ['websocket_channel']}),
    # url('', AsgiHandler),
]

urlpatterns = [
    url('events/', AuthMiddlewareStack(
        URLRouter(django_eventstream.routing.urlpatterns)
    ), {'channels': ['test']}),
    url('', AsgiHandler),
]
