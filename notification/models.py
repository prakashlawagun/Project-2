from django.db import models
from account.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=100)
    message = RichTextField()

    def __str__(self):
        return self.title


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    notify = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name="user_notification")
    created_at = models.DateTimeField(auto_now_add=True)
    seen_by = models.BooleanField(default=False)