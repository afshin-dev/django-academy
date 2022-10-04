from django.urls import path
from playground.views import hi

urlpatterns = [
    path("hi/", hi, name="playground\hi"),
]
