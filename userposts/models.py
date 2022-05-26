from django.db import models
from users.models import UserModel


class Post(models.Model):
    author = models.ForeignKey(UserModel,default = '1', on_delete=models.CASCADE)

    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title
