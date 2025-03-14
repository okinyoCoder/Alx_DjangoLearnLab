from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, readonly=True)

    class meta:
        model = Author
        fields = ['name', 'books']
