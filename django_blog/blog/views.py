from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    return render(request, 'blog/profile.html', {'form': form})