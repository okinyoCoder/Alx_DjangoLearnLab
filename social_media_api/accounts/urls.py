from .views import register, profile, loginView
from django.urls import path

urlpatterns = [
    path('register/', register, name='user-register'),
    path('login/', loginView, name='user-login'),
    path('profile/', profile, name='user-profilr'),
]
