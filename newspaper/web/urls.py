from web.views import *
from django.urls import path, include

urlpatterns = [
    path("", index, name="front-page")
]
