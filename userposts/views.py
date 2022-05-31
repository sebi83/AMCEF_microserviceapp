from django.shortcuts import render
from rest_framework import decorators, viewsets, generics, status, mixins
from rest_framework.response import Response
import requests
from yaml import serialize  # only for API documentation
import json
from users import models
import requests

# usersposts_app
from .models import Post
from .serializers import PostSerializer
from users.serializers import UserSerializer
from users.models import UserModel






# user ID and post json data from external API

URL_POSTS = "https://jsonplaceholder.typicode.com/posts/"
URL_USERS = "https://jsonplaceholder.typicode.com/users/"

posts_fetch = requests.get(
    URL_POSTS, headers={"Content-Type": "application/json"}
).json()

users_fetch = requests.get(
    URL_USERS, headers={"Content-Type": "application/json"}).json()

# users_json = 







class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): 
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def partial_update(self, request, pk=None):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        

    def destroy(self, request, pk=None):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class UsersView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    



    
    # except Post.DoesNotExist:
    #     fetched = post_data_external[pk - 1]
    #     serializer = PostSerializer(data=fetched, many = False)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
