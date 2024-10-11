from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutUs, name="about"),
    path("contact/", views.contactUs),
    path("for/", views.forPage, name="for-page"),
    path("login/", views.loginPage, name="login"),
    path("card/", views.cardView, name="card-page"),
    path("color/", views.cardColor, name="card-color"),
    path("forggg/", views.forGGG, name="for-test"),
]
