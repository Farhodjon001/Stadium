from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class CreateCustomUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer