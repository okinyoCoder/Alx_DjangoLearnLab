from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = '__all__'