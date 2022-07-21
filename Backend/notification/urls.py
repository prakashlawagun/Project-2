from django.urls import path,include
from notification import views
from rest_framework.routers import DefaultRouter
app_name='notification'
router = DefaultRouter()
router.register('notify',views.SendUserNotification)
urlpatterns = [
  path('',include(router.urls)),
  path('status/<int:pk>/',views.ChangeStatusView.as_view(),name="status")
]
