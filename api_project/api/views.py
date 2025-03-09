from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAdminUser, IsAuthenticated

def index(request): 
    return HttpResponse('Welcome to my book store.')

# Define a BookSerializer class that extends rest_framework.serializers.ModelSerializer 
  # and includes all fields of the Book model.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Use rest_framework.viewsets.ModelViewSet, which provides implementations for various actions 
  # like list, create, retrieve, update, and destroy
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
