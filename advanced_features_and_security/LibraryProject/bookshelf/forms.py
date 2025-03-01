from .models import Book
from django.forms import ModelForm

class BookForm(ModelForm):
    class meta:
        model = Book
        field = '__all__'