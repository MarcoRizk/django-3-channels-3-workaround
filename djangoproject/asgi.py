import os

from channels.routing import ProtocolTypeRouter
from configurations import importer

from .routing import ws_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
importer.install()

application = ProtocolTypeRouter({
    "websocket": ws_application,
})
