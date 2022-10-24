from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import *
from foodcart.models import Cart, CartItems
from .serializers import OrdersSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from foodcart.serializers import CartItemSerializer
from account.utils import Util
from .serializers import OrderItemSerializer

class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            queryset = Order.objects.get(id=pk)
            serializers = OrdersSerializers(queryset)
            data = serializers.data
            all_data = []
            cartproduct = OrderItem.objects.get(cart_id=data['cart']['id'])
            cartproduct_serializer = OrderItemSerializer(cartproduct, many=True)
            data['cartproduct'] = cartproduct_serializer.data
            all_data.append(data)
            return Response(data)

        query = Order.objects.filter(cart__user=request.user)
        serializers = OrdersSerializers(query, many=True)
        all_data = []
        for order in serializers.data:
            order_item = OrderItem.objects.filter(cart_id=order['cart']['id'])
            orderitem_serializer = OrderItemSerializer(order_item, many=True)
            order['order_item'] = orderitem_serializer.data
            all_data.append(order)
        return Response(all_data)

    def post(self, request):
        user = request.user
        data = request.data
        cart, _ = Cart.objects.get_or_create(user=user, ordered=False)
        cartitem, _ = CartItems.objects.filter(cart=cart)
        shipping_address = data.get('shipping_address')
        mobile = data.get('mobile')
        email = data.get('email')
        total = cart.total_price
        order_status = "Order Received"
        created_at = data.get('created_at')
        pin = data.get('pin')
        if total != 0:
            order = Order(user=user, cart=cart,product=cartitem.product,shipping_address=shipping_address, mobile=mobile,
                          email=email,
                          total=total,
                          order_status=order_status, created_at=created_at,pin=pin)
            order.save()
            cart_item = CartItems.objects.filter(user=user, cart=cart.id)
            cart_item.delete()

            # data = {
            #     'subject': 'Order Food',
            #     'body':'Your order have received,please wait for delivery',
            #     'to_email': user.email
            # }
            # Util.send_email(data)
        else:
            return Response({'msg': 'Order is failed'})
        return Response({'msg': 'Order is placed'})


class OrderCancel(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        user = request.user
        order_obj = Order.objects.get(id=pk)
        order_obj.delete()
        order_item = OrderItem.objects.get(id=pk)
        order_item.delete()

        # data = {
        #     'subject': 'Order Cancel',
        #     'body': 'You have cancel the order.',
        #     'to_email': user.email
        # }
        # Util.send_email(data)
        return Response({'msg': 'Order Cancel'})
