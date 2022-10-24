from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from menu.models import MealGroup

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_save_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Subscription(models.Model):
    class Period(models.TextChoices):
        WEEKLY = 'Weekly', 'Weekly'
        MONTHLY = 'Monthly', 'Monthly'
        YEARLY = 'Yearly', 'Yearly'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    period = models.CharField(max_length=10, choices=Period.choices, default=Period.WEEKLY)

    def __str__(self):
        return f"{self.user}"

    @property
    def is_active(self):
        return self.end_date > datetime.now().date()

    @classmethod
    def create_subscription(cls, user, period):
        return cls.objects.create(user=user, period=period)

    def save(self, *args, **kwargs):
        if self.start_date is None:
            self.start_date = datetime.now()
        if self.end_date is None:
            if self.period == self.Period.WEEKLY:
                self.end_date = self.start_date + timedelta(days=7)
            elif self.period == self.Period.MONTHLY:
                self.end_date = self.start_date + timedelta(days=30)
            elif self.period == self.Period.YEARLY:
                self.end_date = self.start_date + timedelta(days=365)
        super().save(*args, **kwargs)


class SubscriptionMealGroup(models.Model):
    meal_group = models.ForeignKey(MealGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.meal_group}"
