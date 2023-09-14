from django.urls import path
from .views import CreateStadiumAPIView

urlpatterns=[
    path('create-stadium/',CreateStadiumAPIView.as_view())
]