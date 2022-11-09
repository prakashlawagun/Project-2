from django.urls import path,include
from contact import views
from rest_framework.routers import DefaultRouter
app_name = 'contact'
router = DefaultRouter()
router.register('',views.ContactViewSet,basename="contact")
router.register('reply',views.ReplyViewSet,basename="reply")
urlpatterns = [
  path('',include(router.urls)),
]
