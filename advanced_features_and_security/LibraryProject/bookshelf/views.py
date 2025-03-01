from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, CustomUser
from django.views.generic import ListView, DetailView
from .forms import BookForm
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True) 
class BookDetailView(DetailView):
    model = Book
    template_name = 'bookdetailview.html'
    context_object_name = 'book'

@permission_required('bookshelf.can_add', raise_exception=True) 
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/success/")
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {"form": form})

@permission_required('bookshelf.can_edit', raise_exception=True) 
def edit_book(request, book_id):
    obj = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/success/")
    else:
        form = BookForm(instance=obj)
    return render(request, "bookshelf/edit.html", {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True) 
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('/success/')
    return render(request, 'relationship_app/delete_book.html', {'book': book})