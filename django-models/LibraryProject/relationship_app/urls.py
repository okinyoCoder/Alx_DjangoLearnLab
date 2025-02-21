from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views

urlpatterns = [
    path('book/', views.book_list),
    path('library/', views.LibraryDetailView.as_view()),
]