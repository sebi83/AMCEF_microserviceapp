from rest_framework import serializers
from .models import Post 
from users.models import UserModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'
        

def create(self, validated_data):
    return Post.objects.create(**validated_data) and UserModel.objects.create(**validated_data)



    

def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.body = validated_data.get('body', instance.body)
    instance.userID = validated_data.get('userID', instance.userID)
    instance.id = validated_data.get('id', instance.id)
    instance.save()
    return instance
        
   