from django.shortcuts import render
from .models import Stadium
from .serializers import StadiumSerializers
from rest_framework import generics
from config.permissions import ManagerPermission,AdminPermission

# Create your views here.

class CreateStadiumAPIView(generics.CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializers
    permission_classes = (ManagerPermission,)

