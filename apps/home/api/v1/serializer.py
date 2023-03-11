from __future__ import annotations

from rest_framework import serializers

from apps.home.models import Contact
from apps.home.models import Notification
from apps.home.models import Certificate
from apps.courses.models import CourseVideo
from ...certificaty import certificaty


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

class CertificateSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'user', 'course', 'created_at')






