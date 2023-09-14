from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import *
from .models import *
from Stadium.models import *
from config.permissions import *
from django_filters.rest_framework import DjangoFilterBackend


class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (AdminPermission,)


class DetailByStadiumView(APIView):
    def get(self, *args, **kwargs):
        detail_name = kwargs["detail_name"]
        detail = get_object_or_404(Stadium, name=detail_name)
        detail_view = Order.objects.filter(name=detail.id)
        serializer = OrderSerializers(detail_view, many=True)
        return Response(serializer.data)

