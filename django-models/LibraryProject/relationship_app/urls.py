from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_list),
    path('library/', views.LibraryListView.as_view()),
]