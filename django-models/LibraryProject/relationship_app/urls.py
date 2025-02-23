from django.urls import path, include
from .views import list_books
from .views import LibraryDetailView
from .views import Registration
from . import views

urlpatterns = [
    path('book/', views.book_lists, name='book'),
    path('library/', views.LibraryDetailView.as_view(), name='library'),
    path('register/', views.Registration.as_view(), name='register'),
    path("relationship_app/", include("django.contrib.auth.urls")),
]