from channels.routing import ProtocolTypeRouter, URLRouter
import talk_app.routing
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'http': URLRouter(talk_app.routing.urlpatterns),
    # 'websocket': URLRouter(talk_app.routing.websocket_urlpatterns),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            talk_app.routing.websocket_urlpatterns
        )
    ),
})
