from decimal import Decimal

from django.db import models
from account.models import User
from menu.models import MenuItem
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.name)


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = MenuItem.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    # total_cart_items = CartItems.objects.filter(user=cart_items.user)
    # cart = Cart.objects.get(id=cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()


@receiver(post_delete, sender=CartItems)
def total_price(sender, **kwargs):
    cart_item = kwargs['instance']
    cart = Cart.objects.get(id=cart_item.cart.id)
    cart.total_price -= cart_item.price
    cart.save()
