from .models import Book, Author, Librarian, Library

#Query all books by a specific author.
def get_books_Byauthor(author_name):
    author = Author.objects.get(name=author_name)
    q1 = Book.objects.filter(author=author)
    return q1

#List all books in a library.
def list_library_books(library_name):
    q2 = Library.objects.get(name=library_name)
    return q2.books.all()

#Retrieve the librarian for a library.
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    librarianName = Librarian.objects.get(library=library)
    return librarianName