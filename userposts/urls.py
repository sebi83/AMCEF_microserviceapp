from django.urls import path
from .views import PostViewSet, UserAPI



urlpatterns = [
    path("posts/",
         PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("posts/<int:pk>/",
         PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("users/", UserAPI.as_view()),
    ]



