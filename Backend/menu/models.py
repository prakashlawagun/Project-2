from django.db import models


# Create your models here.
class MealCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='items')
    category = models.ForeignKey(MealCategory, on_delete=models.CASCADE,related_name="menu")
    description = models.CharField(max_length=300)
    calories = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
