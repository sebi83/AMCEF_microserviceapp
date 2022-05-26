from . import views
from django.urls import path
from .views import posts_overview,post_list, post_detail, post_create, post_update, post_delete


urlpatterns = [
    path('', views.posts_overview, name='posts-overview'),
    path('posts/', views.post_list, name='post-detail'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('post-create/', views.post_create, name='post-create'),
    path('post-update/<int:pk>/', views.post_update, name='post-update'),
    path('post-delete/<int:pk>/', views.post_delete, name='post-delete'),
]
