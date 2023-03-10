from __future__ import annotations

from django.urls import include
from django.urls import path


urlpatterns = [
    path('v1/', include('apps.home.api.v1.urls')),
]
