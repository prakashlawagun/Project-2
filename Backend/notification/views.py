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


class ChangeStatusView(APIView):
    def put(self,request,pk=None,format=None):
        id = pk
        notify = UserNotification.objects.get(id=id)
        serializer = UserNotificationSerializer(notify,data=request.data)
        if serializer.is_valid(raise_exception=True):
            if notify.user == request.user:
                notify.seen_by = True
                notify.save()
            return Response({'msg':'Done'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

