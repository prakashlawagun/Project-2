from rest_framework import serializers
from .models import *
from menu.serializers import *
from foodcart.serializers import *


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','cart', 'shipping_address', 'mobile', 'email', 'total', 'order_status', 'created_at']
        depth = 1


class OrderItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'
