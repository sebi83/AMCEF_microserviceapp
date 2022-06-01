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
from .serializers import PostSerializer, UserSerializer
from users.models import UserModel

"""
helper function for fetching external API data
"""


def is_userid_valid(pk: int) -> bool:
    
    URL_USERS = f"https://jsonplaceholder.typicode.com/users/{pk}"
    users_fetched = requests.get(
    URL_USERS,  headers={"Content-Type": "application/json"}).json()
    return bool(users_fetched)


class PostViewSet(viewsets.ModelViewSet):

    """ 
    Posts viewset
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):

        URL_POSTS = f"https://jsonplaceholder.typicode.com/posts/{pk}"

        

        try:
            return Response(data=PostSerializer(Post.objects.get(id=pk)).data)

        except Post.DoesNotExist:
            try:
                posts_fetch = requests.get(
                    URL_POSTS, headers={"Content-Type": "application/json"}
                ).json()

                fetched = posts_fetch
                serializer = PostSerializer(data=fetched, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response(data='Post with id {} does not exist and cannot be fetched.'.format(pk), status=status.HTTP_404_NOT_FOUND)

    def update(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(
            post, data=request.data, partial=True, many=True)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(
            instance=post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersView(viewsets.ModelViewSet):

    """ 
    Users viewset
    """

    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def handle_exception(self, exc):
        return super().handle_exception(exc)

    def list(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        
        if is_userid_valid(request.data['id']):
            
            serializer = UserSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data='User with id {} does not exist in external API users endpoint.'.format(request.data['id']), status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk):

        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
