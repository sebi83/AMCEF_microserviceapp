from django.db import models
from django.contrib.auth.models import User
import requests


class Post(models.Model):
    id = models.IntegerField(primary_key=False)
    userID = models.IntegerField(default=0)
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title
