from __future__ import annotations

from rest_framework import serializers

from apps.home.models import Contact
from apps.home.models import Notification


class ContactSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email',  'message', 'created_at')


class ContactSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'message', 'created_at')

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)


class NotificationSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'title', 'message', 'is_read', 'created_at')


class NotificationSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'title', 'message', 'is_read', 'created_at')

    def create(self, validated_data):
        return Notification.objects.create(**validated_data)
