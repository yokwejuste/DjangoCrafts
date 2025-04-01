from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm, DjangoCaptchaForm, InvisibleForm, V3Form


def home(request):
    return render(request, "home.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Yay! You are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def invisible(request):
    if request.method == "POST":
        form = InvisibleForm(request.POST)
        if form.is_valid():
            return HttpResponse("Yay! You are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")
    else:
        form = InvisibleForm()
    return render(request, "invisible.html", {"form": form})


def v3(request):
    if request.method == "POST":
        form = V3Form(request.POST)
        if form.is_valid():
            return HttpResponse("Yay! You are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")
    else:
        form = V3Form()
    return render(request, "v3.html", {"form": form})


def django_captcha(request):
    if request.method == "POST":
        form = DjangoCaptchaForm(request.POST)
        if form.is_valid():
            return HttpResponse("Yay! You are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")
    else:
        form = DjangoCaptchaForm()
    return render(request, "django_captcha.html", {"form": form})
