from rest_framework import serializers
from .models import Post 
from users.models import UserModel


class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = '__all__' 
        
class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'
        

def create(self, validated_data):
    return Post.objects.create(**validated_data)
        
   