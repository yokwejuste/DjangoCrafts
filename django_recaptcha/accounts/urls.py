from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("invisible/", views.invisible, name="invisible"),
    path("v3/", views.v3, name="v3"),
    path("django-captcha/", views.django_captcha, name="django_captcha"),
]
