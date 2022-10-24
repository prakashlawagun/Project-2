from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SubscriptionMealViewSet

app_name = 'subscription'

router = DefaultRouter()
router.register('', SubscriptionMealViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
]
