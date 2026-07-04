from django.contrib import admin

from .models import (
    AutomationProfile,
    BookingHistory,
)

admin.site.register(AutomationProfile)
admin.site.register(BookingHistory)