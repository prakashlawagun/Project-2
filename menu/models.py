from django.db import models
from django.dispatch import receiver
from account.models import User
from django.db.models.signals import pre_save, post_save
from ckeditor.fields import RichTextField


class MealCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='items', null=True)
    category = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name="menu")
    description = RichTextField()
    calories = models.IntegerField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




