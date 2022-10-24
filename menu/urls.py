from django.urls import path,include
from menu import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('menu',views.MenuItemAPIView,basename="menu")
router.register('category',views.MealCategoryAPIView,basename="category")

urlpatterns = [
  path('search/',views.search_food.as_view()),
  path('',include(router.urls)),
]
