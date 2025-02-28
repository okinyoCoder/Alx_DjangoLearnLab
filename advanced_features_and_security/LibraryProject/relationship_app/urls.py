from django.urls import path
from .views import list_books, admin_view, librarian_view, member_view
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
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name="add_book/"),
    path('books/edit/<int:book_id>/', views.edit_book, name="edit_book/"),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]