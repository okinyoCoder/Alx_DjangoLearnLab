from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

def index(request): 
    return HttpResponse('Welcome to my book store.')

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = 'BookSerializer'