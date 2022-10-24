from rest_framework import serializers

from menu.models import MealCategory, MenuItem, MealGroup


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = ['id', 'name', 'image', ]


class MenuItemSerializer(serializers.ModelSerializer):
    category = MealCategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'photo', 'name', 'category', 'description', 'calories', 'price', 'created_at']


class MealGroupSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['menu_items'] = MenuItemSerializer(instance.menu_items.all(), many=True).data
        return data

    class Meta:
        model = MealGroup
        fields = ['id', ]
