from django.db import models
from userposts.models import Post
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    userID = models.IntegerField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user)
