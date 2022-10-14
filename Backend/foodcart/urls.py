from django.urls import path
from foodcart.views import *

urlpatterns = [
    path('carts/',CartView.as_view())
]
