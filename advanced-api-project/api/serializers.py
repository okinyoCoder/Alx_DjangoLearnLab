from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, data):
        """custom validation to the BookSerializer to 
           ensure the publication_year is not in the future
        """
        thisYear = datetime.datetime.now().year
        if data['publication_year'] > thisYear:
            raise serializers.ValidationError("ensure the publication_year is not in the future")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, readonly=True)

    class meta:
        model = Author
        fields = ['name', 'books']
