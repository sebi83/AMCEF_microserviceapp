from django.db import models
from users.models import UserModel


class Post(models.Model):

    title = models.CharField(max_length=100, default="")
    body = models.CharField(max_length=1000, default="")
    id = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, related_name="userID")

    def __str__(self):
        return self.title
