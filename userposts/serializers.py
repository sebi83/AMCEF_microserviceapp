from rest_framework import serializers
from .models import Post
from users.models import UserModel



class PostSerializer(serializers.ModelSerializer):
    
    
    userID = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), write_only=True)
    title = serializers.CharField(max_length=100, default="")
    body = serializers.CharField(max_length=1000)
    

    class Meta:
        model = Post
        fields =  '__all__'

    def create(self, validated_data):
        
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    
        
    class Meta:
        fields = ('id', 'name', 'username')
        model = UserModel

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.userID)
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance