from ast import Return
from distutils.log import error
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


# users_app
from users.models import UserModel
from users.serializers import UserSerializer

import requests

# user ID and post json data from external API
URL = "https://jsonplaceholder.typicode.com/posts/"
post_data_external = requests.get(
    URL, headers={"Content-Type": "application/json"}
).json()

userid_data = requests.get(
    URL, headers={"Content-Type": "application/json"}).json()


@decorators.api_view(["GET"])
def PostsOverview(request):
    api_urls = {
        "All posts": "posts/",
        "Single post with CRUD": "posts/<int:pk>/",

    }
    return Response(api_urls)


@decorators.api_view(["GET", "POST"])
def PostList(request):

    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET", "DELETE", "PUT", "POST"])
def PostDetail(request, pk):
    try:
        Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        fetched = post_data_external[pk - 1]
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
              
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":

        post.delete()
        return Response("Post deleted.")
