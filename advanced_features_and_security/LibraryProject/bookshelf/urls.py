from django.urls import path
from .views import add_book, edit_book, delete_book, book_detail,example_view
from . import views


urlpatterns = [
    path("exampleForm/", views.example_view, name='example-form'),
    path("book/<int:book_id>", views.book_detail, name='books-details'),
    path("book/add/", views.add_book, name="add-book"),
    path("book/edit/", views.edit_book, name='edit-book'),
    path('book/delete', views.delete_book, name='delete-book'),
]
