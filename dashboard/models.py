from django.db import models


class AutomationProfile(models.Model):
    website_url = models.URLField(
        default="https://learner.saveetha.in/"
    )

    username = models.CharField(
        max_length=150
    )

    password = models.CharField(
        max_length=255
    )

    automation_enabled = models.BooleanField(
        default=False
    )

    headless = models.BooleanField(
        default=False
    )

    retry_count = models.PositiveIntegerField(
        default=3
    )

    refresh_interval = models.PositiveIntegerField(
        default=30
    )

    preferred_event = models.CharField(
        max_length=150,
        blank=True
    )

    preferred_slot = models.CharField(
        max_length=150,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.username


class BookingHistory(models.Model):

    event_name = models.CharField(
        max_length=150
    )

    slot = models.CharField(
        max_length=100
    )

    status = models.CharField(
        max_length=30
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.event_name} - {self.status}"