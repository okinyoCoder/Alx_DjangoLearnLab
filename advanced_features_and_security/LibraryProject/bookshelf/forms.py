from .models import Book
from django.forms import ModelForm
from django import forms

class BookForm(ModelForm):
    class meta:
        model = Book
        field = '__all__'

class ExampleForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    publication_year = forms.IntegerField(default=2020)