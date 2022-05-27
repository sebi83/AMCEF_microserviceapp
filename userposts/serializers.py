from rest_framework import serializers
from .models import Post 
from users.models import UserModel


class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ('title', 'body' )
        
class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = UserModel
        fields = ('id', 'userID')
        
   