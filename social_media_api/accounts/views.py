from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework import status
from .models import CustomUser
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'successful register a user'
            token = Token.objects.get(user=serializer).key
            data['token'] = token
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])   
def profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)

@api_view(["POST"])
def loginView(request):
    if request.method == "POST":
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })