from django.urls import path, include
from .views import list_books
from .views import LibraryDetailView
from .views import Registration, RelationLoginView,RelationLogoutView
from . import views

urlpatterns = [
    path('book/', views.book_lists, name='book'),
    path('library/', views.LibraryDetailView.as_view(), name='library'),
    path('register/', views.Registration.as_view(), name='register'),
    path("login/", RelationLoginView.as_view(), name="login"),
    path("logout/", RelationLogoutView.as_view(), name="logout"),
]