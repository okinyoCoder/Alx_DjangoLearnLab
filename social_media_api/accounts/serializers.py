from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'followers']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        token, created = Token.objects.create(user=user)
        return {'user': user, 'token': token.key}