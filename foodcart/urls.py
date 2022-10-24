from django.urls import path, include

from rest_framework.routers import DefaultRouter
from foodcart.views import CartViewSet

app_name = 'foodcart'

router = DefaultRouter()
router.register('', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]
