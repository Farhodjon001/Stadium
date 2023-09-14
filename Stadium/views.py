from django.shortcuts import render
from .models import Stadium
from .serializers import StadiumSerializers
from rest_framework import generics
from config.permissions import ManagerPermission,AdminPermission

# Create your views here.

class CreateStadiumAPIView(generics.CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializers
    permission_classes = (ManagerPermission, AdminPermission)

class ListManagerStadiumAPIView(generics.ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializers
    permission_classes = (ManagerPermission,)

    def get_queryset(self):
        user = self.request.user
        manager= CustomUser.objects.get(id=user.id)
        return Stadium.objects.filter(manager=manager)

class ListManagerOrders(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (ManagerPermission,)

    def get_queryset(self):
        user=self.request.user
        stadion=Stadium.objects.get(manager=user.id)
        return Order.objects.filter(name=stadion.id)


class ListEptyStadiumByManager(APIView):
    def get(self):
        stadium=Stadium.objects.get(manager=self.request.user.id)
        orders=Order.objects.filter(name=stadium.id)




# class ListEptyStadium(APIView)
#     def get(self, *args, **kwargs):
#         begin_time = kwargs["begin_time"]
#         end_time = kwargs["end_time"]
#
#         oders=Order.objects.filter(begin_time=)
#         detail_view = Order.objects.filter(name=detail.id)
#         serializer = OrderSerializers(detail_view, many=True)
#         return Response(serializer.data)