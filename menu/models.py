from ckeditor.fields import RichTextField
from django.db import models
from account.models import User


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


class MealGroup(models.Model):
    name = models.CharField(max_length=100)
    menu_items = models.ManyToManyField(MenuItem, related_name="meal_group")

    def __str__(self):
        return self.name
