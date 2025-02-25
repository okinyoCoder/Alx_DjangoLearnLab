from django.shortcuts import render, redirect
from .models import Library, UserProfile, Book
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

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

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('list_books')
    else:
      form = UserCreationForm()
  return render(request, 'relationship_app/register.html', {'form': form})

#Utilize Django’s built-in views and forms for handling user login
#class RelationLoginView(LoginView):
#    template_name = 'relationship_app/login.html'
#Utilize Django’s built-in views and forms for handling user logout
#class RelationLogoutView(LogoutView):
#    template_name = 'relationship_app/logout.html'


#Admin view that only users with the ‘Admin’ role can access
@user_passes_test(is_admin)
def admin_view(request):
   return render(request, "relationship_app/admin_view.html")

#Librarian view accessible only to users identified as Librarians
@user_passes_test(is_librarian)
def librarian_view(request):
   return render(request, "relationship_app/librarian_view.html")

#Member view for users with the Member role
@user_passes_test(is_member)
def member_view(request):
   return render(request, "relationship_app/member_view.html")

def is_admin(user):
  return user.userprofile.role == "Admin"

def is_librarian(user):
  return user.userprofile.role == "Librarian"

def is_member(user):
  return user.userprofile.role == "Member"
