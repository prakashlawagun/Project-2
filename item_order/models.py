from django.db import models

from account.models import User
from foodcart.models import Cart, CartItems
from menu.models import MenuItem

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=200)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    pin = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user.username} order{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart_item = models.OneToOneField(CartItems, on_delete=models.CASCADE)
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"{self.order.user} Order Item"
