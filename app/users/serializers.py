from rest_framework import serializers
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }