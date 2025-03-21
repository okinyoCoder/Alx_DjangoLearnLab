from django.urls import path, include
from .views import SignUpView
from django.views.generic import TemplateView

urlpatterns = [
    path('',  include('django.contrib.auth.urls')),
    path('profile/',
             TemplateView.as_view(template_name='blog/profile.html'),
             name='profile'),
    path("register/", SignUpView.as_view(), name="blog/signup"),
]