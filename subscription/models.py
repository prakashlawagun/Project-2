from datetime import datetime, timedelta
from django.db import models
from account.models import User
from menu.models import MealGroup


class Subscription(models.Model):
    class Period(models.TextChoices):
        WEEKLY = 'Weekly', 'Weekly'
        MONTHLY = 'Monthly', 'Monthly'
        YEARLY = 'Yearly', 'Yearly'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(blank=True, null=True)
    period = models.CharField(max_length=10, choices=Period.choices, default=Period.WEEKLY)
    amount = models.PositiveIntegerField(default=0)

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
