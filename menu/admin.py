from django.contrib import admin
from django.db.models import Sum
from django.utils.safestring import mark_safe

from .models import MealCategory, MenuItem, MealGroup


@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'photo',
        'category',
        'description',
        'calories',
        'price',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(MealGroup)
class MealGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'meal_items', 'total_calories',)
    search_fields = ('name',)

    @staticmethod
    def meal_items(obj):
        names = obj.menu_items.values_list('name', flat=True)
        html = '<ul class="list-group">'
        for name in names:
            html += f'<li class="list-group-item">{name}</li>'
        html += '</ul>'
        return mark_safe(html)

    @staticmethod
    def total_calories(obj):
        calories = obj.menu_items.aggregate(total=Sum('calories'))
        return calories['total']
