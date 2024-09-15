from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets
from .serializer import BlogSerializer
from .models import Blog
# Create your views here.
class BlogListview(ListView):
    model = Blog
    fields = [
        'topic',
        'body'
    ]
    template_name = 'cocoaApp/list.html'
    
class BlogCreateview(CreateView):
    model = Blog
    fields = ['topic','body']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/'
    
class BlogDeleteview(DeleteView):
    model = Blog
    template_name = 'cocoaApp/delete.html'
    success_url = '/'
class BlogUpdateview(UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/'
    
class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
# views.py
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({"message": "Connexion réussie"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Nom d'utilisateur ou mot de passe incorrect."}, status=status.HTTP_400_BAD_REQUEST)


# views.py
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import serializers

# Serializer pour l'utilisateur
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash le mot de passe
        user.save()
        return user

# Vue pour créer un utilisateur
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Utilisateur créé avec succès"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

def add_user_to_group(username, group_name):
    user = User.objects.get(username=username)
    group = Group.objects.get(name=group_name)
    group.user_set.add(user)
    


