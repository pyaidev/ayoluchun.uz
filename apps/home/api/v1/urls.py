from __future__ import annotations

from django.urls import path

from .views import ContactCreateView
from .views import ContactListView
from .views import NotificationCreateView
from .views import NotificationListView
from .views import CertificateListView

urlpatterns = [
    path('notification/', NotificationListView.as_view(), name='notification-list'),
    path(
        'notification/create/', NotificationCreateView.as_view(),
        name='notification-create',
    ),
    path('contact/', ContactListView.as_view(), name='contact-list'),
    path('contact/create/', ContactCreateView.as_view(), name='contact-create'),
    path('certificate/', CertificateListView.as_view(), name='certificate-list'),
]
