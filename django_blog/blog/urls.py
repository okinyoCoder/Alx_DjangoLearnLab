from django.urls import path, include
from .views import SignUpView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',  include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/',
             TemplateView.as_view(template_name='blog/profile.html'),
             name='profile'),
    path("register/", SignUpView.as_view(), name="blog/register"),
]