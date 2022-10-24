from django.db import models

from account.models import User
from foodcart.models import Cart, CartItems
from menu.models import MenuItem


class Order(models.Model):
    class Status(models.TextChoices):
        ORDER_RECEIVED = "Order Received", "Order Received"
        ORDER_PROCESSING = "Order Processing", "Order Processing"
        ON_THE_WAY = "On the way", "On the way"
        ORDER_COMPLETED = "Order Completed", "Order Completed"
        ORDER_CANCELED = "Order Canceled", "Order Canceled"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=Status.choices, default=Status.ORDER_RECEIVED)
    created_at = models.DateTimeField(auto_now_add=True)

    # Contact details
    shipping_address = models.CharField(max_length=200)
    mobile = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user.username} order{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name="order_items")
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"{self.order.user} Order Item"
