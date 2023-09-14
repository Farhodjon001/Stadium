from .models import *
from rest_framework import serializers
from customuser.models import CustomUser


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CreateOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ('name', 'begin_time', 'end_time', 'status')

    def create(self, validated_data):
        print(self.context['request'].user.id)
        validated_data["user"] = CustomUser.objects.get(id=self.context['request'].user.id)
        return super(CreateOrderSerializers, self).create(validated_data)
