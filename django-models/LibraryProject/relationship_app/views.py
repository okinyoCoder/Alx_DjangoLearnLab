from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.

#Create a function-based view that lists all books stored in the database
def book_lists(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

#class-based view that displays details for a specific library, 
# listing all books available in that library.
class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
    context_object_name = 'library'

#Utilize Django’s built-in views and forms for handling user registration.
class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

#Utilize Django’s built-in views and forms for handling user login
#class RelationLoginView(LoginView):
#    template_name = 'relationship_app/login.html'
#Utilize Django’s built-in views and forms for handling user logout
#class RelationLogoutView(LogoutView):
#    template_name = 'relationship_app/logout.html'