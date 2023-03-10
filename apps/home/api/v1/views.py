from __future__ import annotations

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from .serializer import ContactSerializerGet
from .serializer import ContactSerializerPost
from .serializer import NotificationSerializerGet
from .serializer import NotificationSerializerPost
from apps.home.models import Contact
from apps.home.models import Notification


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializerGet
    permission_classes = (IsAuthenticated, IsAdminUser)



    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializerPost
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializerGet
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NotificationCreateView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializerPost
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
