from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('rooms', api.get_rooms),
    # url('make_rooms', api.make_rooms)
]