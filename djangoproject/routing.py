from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
from django.conf.urls import url

from .consumers import EchoConsumer

websocket_urlpatterns = [
    url(r"^ws/chat/admin/$", EchoConsumer.as_asgi()),
]
ws_application = AuthMiddlewareStack(
    URLRouter(websocket_urlpatterns),
)
