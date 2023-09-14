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
        begin_time=validated_data["begin_time"]
        end_time=validated_data['end_time']

        validated_data["user"] = CustomUser.objects.get(id=self.context['request'].user.id)
        if begin_time>=datetime.now() and end_time>datetime.now():
            validated_data["status"] = 1
        else:
            validated_data["status"]=0
        return super(CreateOrderSerializers, self).create(validated_data)
