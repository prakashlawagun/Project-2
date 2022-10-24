from rest_framework import serializers

from foodcart.serializers import MenuItemSerializer

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['order_items'] = OrderItemSerializer(instance.order_items.all(),
                                                  many=True).data
        return data

    class Meta:
        model = Order
        fields = [
            'id',
            'shipping_address',
            'mobile',
            'total',
            'order_status',
            'created_at',
        ]
        read_only_fields = ['id', 'total', 'created_at', 'order_status']


class OrderItemSerializer(serializers.ModelSerializer):
    product = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = [
            'product',
            'quantity',
            'price',
        ]
        read_only_fields = ['order', 'product', 'quantity', 'price']
