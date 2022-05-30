from django.db import models
import requests
import json



class Post(models.Model):
    
    title = models.CharField(max_length=100, default="")
    body = models.TextField(max_length=1000, default="")
    id = models.IntegerField(primary_key=True)
    userID = models.IntegerField(primary_key=False, blank=True, null=True, default=None)

    def __str__(self):
        return self.title
