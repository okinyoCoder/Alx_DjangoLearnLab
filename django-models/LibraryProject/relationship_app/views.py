from django.shortcuts import render
from .models import Book
from .models import Library
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

#Create a function-based view that lists all books stored in the database
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

#class-based view that displays details for a specific library, 
# listing all books available in that library.
class LibraryListView(ListView):
    template_name = 'relationship_app/library_detail.html'
    model = Library