from rest_framework import serializers
from .models import Tag, Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag')


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    
    class Meta:
        model = Post
        fields = ('id', 'user_id','title', 'description', 'create_date', 'image', 'tags')
        