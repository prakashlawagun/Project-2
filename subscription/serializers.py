from rest_framework.serializers import ModelSerializer

from menu.serializers import MealGroupSerializer
from .models import SubscriptionMealGroup


class SubscriptionMealGroupSerializer(ModelSerializer):
    meal_group = MealGroupSerializer()

    def to_representation(self, instance: SubscriptionMealGroup):
        data = super().to_representation(instance)
        data['name'] = instance.meal_group.name
        return data

    class Meta:
        model = SubscriptionMealGroup
        fields = ['meal_group', ]
