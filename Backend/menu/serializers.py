from rest_framework import serializers
from menu.models import MealCategory, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'category', 'description', 'calories', 'created_at']


class MealCategorySerializer(serializers.ModelSerializer):
    menu = MenuItemSerializer(many=True, read_only=True, source='menu_set')

    class Meta:
        model = MealCategory
        fields = ['id', 'name','image','menu']
