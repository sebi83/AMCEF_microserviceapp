from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework import status
import requests
from yaml import serialize  # only for API documentation
import json

# usersposts_app
from .models import Post
from .serializers import PostSerializer
from .services import get_data  # JSON data from API in services.py

# users_app
from users.models import UserModel
from users.serializers import UserSerializer

import requests

# user ID and post json data from external API
URL = 'https://jsonplaceholder.typicode.com/posts/'
post_data = requests.get(URL, headers={'Content-Type':
                                       'application/json'}).json()

userid_data = requests.get(URL, headers={'Content-Type':
                                         'application/json'}).json()


@decorators.api_view(["GET"])
def posts_overview(request):
    api_urls = {
        'Posts': 'posts/',
        'Post details': 'posts/<int:pk>/',
        'Create': 'post-create/',
        'Update': 'post-update/<int:pk>/',
        'Delete': 'post-delete/<int:pk>/',
    }
    return Response(api_urls)


@decorators.api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


@decorators.api_view(["GET", "POST"])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(post, many=False)
    if serializer.is_valid():
        serializer.save()   

    return Response(serializer.data)


@decorators.api_view(["GET", "POST"])
def post_create(request):
    try:
        Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(data=request.data)

    if 
    elif serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@decorators.api_view(["GET", "POST", "PUT"])
def post_update(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["DELETE"])
def post_delete(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    post.delete()
    return Response('Post deleted.')
