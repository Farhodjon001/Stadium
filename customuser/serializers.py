from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class CustomUserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'roles')

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            roles=validated_data.get('roles')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user