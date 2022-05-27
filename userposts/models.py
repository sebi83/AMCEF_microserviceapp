from django.db import models
from users.models import UserModel
import requests
import json



class Post(models.Model):
    
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(max_length=1000, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    userID = models.IntegerField(primary_key=False, blank=True, null=True)

    def __str__(self):
        return self.title
