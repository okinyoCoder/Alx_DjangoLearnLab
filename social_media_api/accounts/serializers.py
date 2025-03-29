from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'followers']