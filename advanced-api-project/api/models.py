from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.DateField
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)