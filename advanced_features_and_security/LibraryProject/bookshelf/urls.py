from django.urls import path
from .views import add_book, edit_book, delete_book, book_detail
from . import views


urlpatterns = [
    path("book/<int:book_id>", views.book_detail, name='books-details'),
    path("book/add/", views.add_book, name="add-book"),
    path("book/edit/", views.edit_book, name='edit-book'),
    path('book/delete', views.delete_book, name='delete-book'),
]
