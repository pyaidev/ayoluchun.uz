from __future__ import annotations

from rest_framework import serializers

from apps.blog.models import Blog
from apps.blog.models import Category


class BlogSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id', 'author', 'position', 'title',
            'category', 'image', 'description', 'views',
        )


class BlogSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id', 'author', 'position', 'title',
            'category', 'image', 'description', 'views',
        )

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


class BlogSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id', 'author', 'position', 'title',
            'category', 'image', 'description', 'views',
        )

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.position = validated_data.get('position', instance.position)
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get(
            'description', instance.description,
        )
        instance.views = validated_data.get('views', instance.views)
        instance.save()
        return instance


class BlogSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id', 'author', 'position', 'title',
            'category', 'image', 'description', 'views',
        )

    def delete(self, instance):
        instance.delete()
        return instance


class CategorySerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class CategorySerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
