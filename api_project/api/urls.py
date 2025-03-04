from django.urls import path
from . import views
from .views import BookList

urlpatterns = [
    path("", views.index, name="index"),
    path('books/', BookList.as_view(), name='book-list'),
]