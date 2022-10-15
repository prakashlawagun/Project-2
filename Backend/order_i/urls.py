from django.urls import path
from order_i.views import *

urlpatterns = [
    path('carts/',CheckoutView)
]
