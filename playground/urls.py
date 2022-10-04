from django.urls import path
from playground.views import hi, tmpl_hi

urlpatterns = [
    path("hi/", hi, name="playground\hi"),
    path("tmpl_hi/", tmpl_hi, name="playground\tmpl_hi"),
]
