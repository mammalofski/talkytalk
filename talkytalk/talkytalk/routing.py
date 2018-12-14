from channels.routing import ProtocolTypeRouter, URLRouter
import talk_app.routing

application = ProtocolTypeRouter({
    'http': URLRouter(talk_app.routing.urlpatterns),
})