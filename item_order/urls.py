from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CancelOrderViewSet

app_name = 'item_order'

router = DefaultRouter()
router.register('', OrderViewSet, basename='order')
router.register('cancel', CancelOrderViewSet, basename='cancel_order')

urlpatterns = [
    path('', include(router.urls)),
]
