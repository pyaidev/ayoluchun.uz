from __future__ import annotations

from django.db import models

from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class Notification(BaseModel):
    user = models.ForeignKey(
        'accounts.Account', on_delete=models.CASCADE, related_name='notifications',
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-id']

    def __str__(self):
        return self.title


class Certificate(BaseModel):
    user = models.ForeignKey(
        'accounts.Account', on_delete=models.CASCADE, related_name='certificates',
    )
    course = models.ForeignKey(
        'courses.Course', on_delete=models.CASCADE, related_name='certificates',
    )
    image = models.ImageField(upload_to='certificates/')

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return self.user.username
