from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CustomUser(AbstractUser):
    # Optional: Add custom fields later
    pass


class ExceptionError(models.Model):
    error_type = models.CharField(max_length=100)
    message = models.TextField()
    traceback = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.error_type} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
