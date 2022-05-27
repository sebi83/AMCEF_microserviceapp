from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'userID')
        model = UserModel

def create (self, validated_data):
    return UserModel.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.userID = validated_data.get('userID', instance.userID)
    instance.id = validated_data.get('id', instance.id)
    instance.save()
    return instance