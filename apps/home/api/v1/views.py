from __future__ import annotations

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from .serializer import ContactSerializerGet
from .serializer import ContactSerializerPost
from .serializer import NotificationSerializerGet
from .serializer import NotificationSerializerPost
from .serializer import CertificateSerializerGet
from apps.courses.models import CourseLesson
from apps.home.models import Contact
from apps.home.models import Notification
from apps.home.models import Certificate
from ...certificaty import certificaty
from apps.accounts.models import Purchased_course


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

    def clean(self):
        if self.request.user.is_authenticated:
            Notification.objects.filter(user=self.request.user).update(is_read=False)


class NotificationCreateView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializerPost
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CertificateListView(generics.ListAPIView):
    queryset = Purchased_course.objects.all()
    serializer_class = CertificateSerializerGet
    permission_classes = (IsAuthenticated,)


    def generate_certificate(self):
        if self.request.user.is_authenticated:
            # print(self.request.user)
            if CourseLesson.objects.filter(lesson_status="Ko'rilgan"):
                certificaty(name=Purchased_course.user_id, course = self.request.user)

    def get(self, request, *args, **kwargs):
        # print("Hello")
        self.generate_certificate()
        return self.list(request, *args, **kwargs)
