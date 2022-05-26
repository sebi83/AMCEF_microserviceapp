from django.db import models


class UserModel(models.Model):
    id = models.IntegerField(primary_key=True)
    userID = models.IntegerField(primary_key=False)

    def __str__(self):
        return str(self.id)
