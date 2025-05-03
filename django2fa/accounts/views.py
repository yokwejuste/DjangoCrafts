from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse

@login_required
def logout_view(request):
    logout(request)
    return redirect('two_factor:login')

def index(request):
    return HttpResponse("Hello, Click the button to confirm you are human, Hummm!!!")


