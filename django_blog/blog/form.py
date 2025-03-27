from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'rows': 3, 'placeholder': 'Write a comment...'})