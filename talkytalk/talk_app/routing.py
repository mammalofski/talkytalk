from django.conf.urls import url
from channels.routing import URLRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
import django_eventstream
from . import consumers

ws_urlpatterns = [
    # url(r'^chat/(?P<username>[^/]+)$', consumers.ChatConsumer),
    url(r'^$', consumers.ChatConsumer),
]

websocket_urlpatterns = [
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    url('ws/', AuthMiddlewareStack(
        URLRouter(ws_urlpatterns)
    ), {'channels': ['websocket_channel']}),
    url('', AsgiHandler),
]

urlpatterns = [
    url('events/', AuthMiddlewareStack(
        URLRouter(django_eventstream.routing.urlpatterns)
    ), {'channels': ['test']}),
    url('', AsgiHandler),
]
