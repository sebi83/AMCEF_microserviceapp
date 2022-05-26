
from django.urls import path, include
from .views import PostsView, PostDetail
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostsView.as_view(), name='post_list'),
    
]
