from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = "__all__"