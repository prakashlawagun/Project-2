from django.shortcuts import render
from notification.serializers import UserNotificationSerializer
from notification.models import UserNotification
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class SendUserNotification(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer


