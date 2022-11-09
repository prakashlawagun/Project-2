from django.urls import path,include
from menu import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('menu',views.MenuItemAPIView,basename="menu")
router.register('category',views.MealCategoryAPIView,basename="category")
router.register('search',views.SearchViewSet,basename="search")

urlpatterns = [
  path('',include(router.urls)),
]
