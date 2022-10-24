from django.urls import path
from .views import *

urlpatterns = [
    path('orders/',OrderCreateView.as_view()),
    path('orders/<int:pk>/',OrderCreateView.as_view()),
    path('order-cancel/<int:pk>/',OrderCancel.as_view()),

]
