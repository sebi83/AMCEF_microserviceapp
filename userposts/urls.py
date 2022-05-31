from django.urls import path, include
from .views import PostViewSet, UsersView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'users', UsersView, basename='users')


urlpatterns = router.urls
