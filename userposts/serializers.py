from rest_framework import serializers
from .models import Post 

class PostSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'userID', 'title', 'body')
        model = Post
        
   