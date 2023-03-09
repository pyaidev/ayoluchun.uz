from rest_framework import serializers
from apps.blog.models import Blog, Category


class BlogGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'category', 'description', 'views', 'created_at']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'category', 'description', 'views', 'created_at']
        extra_kwargs = {
            'views': {'read_only': True}
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']



