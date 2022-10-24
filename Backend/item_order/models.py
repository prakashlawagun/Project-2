from django.db import models
from foodcart.models import Cart, CartItems
from account.models import User
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
from menu.models import MenuItem

# Create your models here.
ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=200)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    pin = models.IntegerField()

    def __str__(self):
        return str(self.user.username) + " " + "order" + str(self.id)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username) + " " + "Order Item"
