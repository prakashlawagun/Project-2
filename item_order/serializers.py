from rest_framework import serializers
from .models import *
from menu.serializers import *
from foodcart.serializers import *


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'cart', 'product', 'shipping_address', 'mobile', 'email', 'total', 'order_status',
                  'created_at',
                  "pin", ]
        depth = 1


class OrderItemSerializer(serializers.ModelSerializer):
    product = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = ['user', 'order', ]
