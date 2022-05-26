from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'userID')
        model = UserModel
