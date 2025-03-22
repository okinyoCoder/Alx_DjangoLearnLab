from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from .form import CreatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Authentication Views create User
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

@login_required
def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    template_name = 'blog/profile.html'
    context = {'user': user}
    return render(request, template_name, context)
  
@login_required
def edit_profile(request, user_id):
    obj = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        form = UserCreationForm(instance=obj)
    return render(request, 'blog/register.html', {'form': form})

# CRUD View Setup
class PostListView(ListView):
    model = Post
    template_name = 'blog/list_post.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url=reverse_lazy('post-list')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post.html'
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)