from .models import *
from rest_framework import serializers
from customuser.models import CustomUser


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CreateOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('name', 'begin_time', 'end_time')

    def create(self, validated_data):
        print(self.context['request'].user.id)
        validated_data["user"] = CustomUser.objects.get(id=self.context['request'].user.id)
        validated_data["status"] = 1
        return super(CreateOrderSerializers, self).create(validated_data)
