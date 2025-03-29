from django.urls import path, include
from accounts.views import login_view, logout_view, home_view, generate_sso_token

urlpatterns = [
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('generate-sso-token/', generate_sso_token, name='generate_sso_token'),
]
