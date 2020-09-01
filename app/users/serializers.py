from rest_framework import serializers
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        username=validated_data.get('username')
        password=validated_data.get('password')
        return User.objects.create_user(username=username,
                                        password=password)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }