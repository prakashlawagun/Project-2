from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from foodcart.models import Cart, CartItems
from .serializers import CartSerializer, CartItemSerializer


class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return CartItems.objects.filter(cart=cart)

    def list(self, request, *args, **kwargs):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        serializer = CartSerializer(cart)
        return Response(
            {
                'message': 'Cart items fetched successfully',
                **serializer.data
            }
        )

    def create(self, request, *args, **kwargs):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response({
                'message': 'Item added to your cart',
                **serializer.data,
            })
        return Response(serializer.errors)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            # Prevent update of product.
            serializer.save(product=instance.product)
            return Response({
                'message': 'Item updated.',
                **serializer.data,
            })
        return Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        self.perform_destroy(instance)
        return Response({
            'message': 'Item deleted from your cart',
            'id': instance_id,
        })
