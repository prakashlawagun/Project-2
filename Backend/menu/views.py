from django.shortcuts import render
from menu.serializers import MealCategorySerializer, MenuItemSerializer
from menu.models import MealCategory, MenuItem
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MealCategoryAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class MenuItemAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer







# class MealCategoryAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         category = MealCategory.objects.all()
#         serializer = MealCategorySerializer(category, many=True)
#         data = serializer.data
#         return Response(data)
#
#
# class MenuItemAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self,request,format=None):
