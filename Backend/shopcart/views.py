from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from shopcart.models import *
from menu.models import MenuItem
from .serializers import *


# Create your views here.


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, ordered=False)
        item = MenuItem.objects.get(id=data.get('item'))
        price = item.price
        quantity = data.get('quantity')
        cart_items = CartItems(cart=cart, user=user, item=item, price=price, quantity=quantity)
        cart_items.save()

        total_price = 0
        cart_items = CartItems.objects.filter(user=user, cart=cart.id)
        for elements in cart_items:
            total_price += elements.price
        cart.total_price = total_price
        cart.save()

        return Response({'success': 'Item Added to your cart'})

    def put(self, request):
        data = request.data
        cart_item = CartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'Success': 'Item Updated'})

    def delete(self, request):
        user = request.user
        data = request.data
        cart_item = CartItems.objects.get(id=data.get('id'))
        cart_item.delete()
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)
