from rest_framework import serializers
from .models import *
from menu.serializers import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    item = MenuItemSerializer()

    class Meta:
        model = CartItems
        fields = '__all__'
