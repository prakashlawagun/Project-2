from django.contrib import admin
from menu.models import MealCategory, MenuItem


# Register your models here.
@admin.register(MealCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'calories', 'created_at']
