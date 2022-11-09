from django.shortcuts import render
from notification.serializers import UserNotificationSerializer
from notification.models import UserNotification
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class SendUserNotification(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

