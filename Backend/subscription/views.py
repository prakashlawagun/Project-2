from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from subscription.serializers import *
from subscription.models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PackageAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Packages.objects.all()
    serializer_class = PackageSerializer


