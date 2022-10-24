from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from foodcart.models import Cart, CartItems
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response({
            'message': 'Order List fetched successfully',
            'data': serializer.data,
        })

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    'message': 'Invalid data',
                    'errors': serializer.errors,
                },
                status=400)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItems.objects.filter(cart=cart)
        if not cart_items.exists():
            return Response({
                'message': 'Cart is empty',
            })

        order = Order.objects.create(
            user=request.user,
            mobile=serializer.validated_data['mobile'],
            shipping_address=serializer.validated_data['shipping_address'],
            total=0,
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.price,
            )
            # Adding the price of each item in the cart to the total price of the order.
            order.total += cart_item.price
            order.save()
            cart_item.delete()

        return Response({
            'message': 'Order created successfully',
            'data': OrderSerializer(order).data,
        })

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        if not order:
            return Response({
                'message': 'Order not found',
            })
        if order.user != request.user:
            return Response({
                'message': 'You do not have permission to view this order',
            })

        serializer = OrderSerializer(order)
        return Response({
            'message': 'Order fetched successfully',
            'data': serializer.data,
        })


class CancelOrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    http_method_names = ['put']

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user).order_by('-created_at')

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if not order:
            return Response({
                'message': 'Order not found',
            })
        if order.user != request.user:
            return Response({
                'message': 'You do not have permission to cancel this order',
            })

        order.order_status = Order.Status.ORDER_CANCELED
        order.save()
        return Response({
            'message': 'Order canceled successfully',
            'data': OrderSerializer(order).data,
        })
