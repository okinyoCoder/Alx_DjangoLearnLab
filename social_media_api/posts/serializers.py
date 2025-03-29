from .models import Post, Comment, CustomUser
from rest_framework import serializers
from accounts.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(many=True, read_only=True)
    class meta:
        model = Post
        fields = ['id', 'author', 'title','content']

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    author = CustomUserSerializer(many=True, read_only=True)
    class meta:
        model = Comment
        fields = ['id', 'author', 'content', 'post']