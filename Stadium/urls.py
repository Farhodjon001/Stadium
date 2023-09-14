from django.urls import path
from .views import CreateStadiumAPIView,ListManagerStadiumAPIView,ListManagerOrdersApiView

urlpatterns=[
    path('create-stadium/',CreateStadiumAPIView.as_view()),
    path('list/manager-stadium/',ListManagerOrdersApiView.as_view()),
    path("list/msnager-stadiums/",ListManagerStadiumAPIView.as_view())
]