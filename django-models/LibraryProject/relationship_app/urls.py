from django.urls import path, include
from .views import list_books
from .views import LibraryDetailView
from .views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('book/', views.book_lists, name='book'),
    path('library/', views.LibraryDetailView.as_view(), name='library'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]