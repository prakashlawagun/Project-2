from account.models import User
from django.db import models

from menu.models import MenuItem


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"{self.user}"

    @property
    def total_price(self) -> float:
        # sourcery skip: inline-immediately-returned-variable, sum-comprehension
        cart_items = self.cart_items.all()
        total = 0
        for cart_item in cart_items:
            total += cart_item.price
        return total


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cart.user} {self.product.name}"

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.product.price
        super().save(*args, **kwargs)
