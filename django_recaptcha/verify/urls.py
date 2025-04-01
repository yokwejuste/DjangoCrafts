from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path("", include("accounts.urls")),
]
