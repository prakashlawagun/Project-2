from rest_framework import serializers

from menu.serializers import MenuItemSerializer
from .models import CartItems, Cart


class CartSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        response = super().to_representation(instance)
        cart_items = CartItems.objects.filter(cart=instance)
        items_count = cart_items.count()
        serializer = CartItemSerializer(cart_items, many=True)
        response['items_count'] = items_count
        response['cart_items'] = serializer.data
        return response

    class Meta:
        model = Cart
        fields = [
            'total_price',
        ]


class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True, min_value=1, )
    cart_item_price = serializers.FloatField(source='price', read_only=True)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = MenuItemSerializer(instance.product).data
        return response

    class Meta:
        model = CartItems
        fields = (
            'id',
            'product',
            'cart_item_price',
            'quantity',
        )
