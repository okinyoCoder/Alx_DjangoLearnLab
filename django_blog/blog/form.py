from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long")
        return content