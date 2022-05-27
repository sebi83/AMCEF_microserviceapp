from . import views
from django.urls import path
from .views import PostDetail, PostList, PostsOverview

urlpatterns = [
    path('', views.PostsOverview, name='posts-overview'),
    path('posts/', views.PostList, name='post-detail'),
    path('posts/<int:pk>/', views.PostDetail, name='post-detail'),
    ]

