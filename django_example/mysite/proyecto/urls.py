from django.urls import path
from proyecto import views


urlpatterns = [
    path("", views.index),
    path("asdf", views.index),
]
