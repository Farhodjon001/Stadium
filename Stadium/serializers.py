from rest_framework import serializers
from .models import Stadium
from customuser.models import CustomUser
class StadiumSerializers(serializers.ModelSerializer):
    class Meta:
        model=Stadium
        fields=('name','price','adress','contact','photo')

    def create(self, validated_data):
        print(self.context['request'].user.id)
        validated_data["manager"]=CustomUser.objects.get(id=self.context['request'].user.id)
        return super(StadiumSerializers,self).create(validated_data)

