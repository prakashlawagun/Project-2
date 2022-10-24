from django.urls import path,include
from subscription import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('packages',views.PackageAPIView,basename="package")

urlpatterns = [
  path('',include(router.urls)),
]
