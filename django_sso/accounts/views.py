from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import SSOUserToken
import uuid

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def generate_sso_token(request):
    if request.method == 'POST':
        user = request.user
        expires_at = timezone.now() + timezone.timedelta(hours=1)
        token = str(uuid.uuid4())
        SSOUserToken.objects.create(
            user=user,
            token=token,
            expires_at=expires_at
        )
        return render(request, 'sso_token.html', {'token': token})
    return redirect('home')
