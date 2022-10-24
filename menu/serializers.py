from rest_framework import serializers

from menu.models import MealCategory, MenuItem


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = ['id', 'name', 'image', ]


class MenuItemSerializer(serializers.ModelSerializer):
    category = MealCategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'photo', 'name', 'category', 'description', 'calories', 'price', 'created_at']


