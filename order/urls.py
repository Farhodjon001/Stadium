from django.urls import path
from .views import *

urlpatterns=[
    path('delete/<int:pk>', OrderDeleteView.as_view()),
    path('detail/<str:detail_name>', DetailByStadiumView.as_view()),
]