from django.shortcuts import render
from account.models import User
from rest_framework.response import Response
from account.serializers import UserRegistrationSerializer, UserLoginSerializer
from account.renderers import UserRenderer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView


# Create your views here.
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'msg': 'Login Success'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'errors': {'non_fields_errors': ['Email or Password is not match']}},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({'msg': 'Login Success'}, status=status.HTTP_201_CREATED)
