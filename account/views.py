from django.shortcuts import render
from django.contrib.auth import get_user_model


from rest_framework import generics

from .serializer import UserSerializers


User= get_user_model()
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers