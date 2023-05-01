from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="Home"),
    path("home/about", views.about, name="About"),
    path("home/password", views.password, name="Pass"),
]