from django.shortcuts import render
from menu.serializers import MealCategorySerializer, MenuItemSerializer
from menu.models import MealCategory, MenuItem, MealGroup
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class MealCategoryAPIView(viewsets.ModelViewSet):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class MenuItemAPIView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

    def retrieve(self, request, *args, **kwargs):
        item = MenuItem.objects.filter(
            calories__range=(100,200),
        ).order_by('calories')
        serializer = MenuItemSerializer(item, many=True)
        return Response(serializer.data)
