from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreateCustomUser.as_view())
]