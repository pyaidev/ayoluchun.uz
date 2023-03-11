from __future__ import annotations

from django.contrib import admin

from .models import Account
from .models import UserProfile
from .models import Purchased_course

# Register your models here.


admin.site.register(Account)
admin.site.register(UserProfile)
admin.site.register(Purchased_course)