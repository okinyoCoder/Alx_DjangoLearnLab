from .models import Book, Author, Librarian, Library

#Query all books by a specific author.
def get_books_Byauthor(authorName):
    q1 = Book.objects.filter(author__name=authorName)
    return q1

#List all books in a library.
def list_library_books():
    return Library.objects.all()

#Retrieve the librarian for a library.
def get_librarian(libraryName):
    q3 = Librarian.objects.filter(library__name=libraryName)
    return q3