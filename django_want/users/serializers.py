from rest_framework import serializers
from django.contrib.auth.models import User, Group


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        return User.objects.create_user(username=username,
                                        password=password)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        return User.objects.create_user(username=username, email=email, password=password,
                                        first_name=first_name, last_name=last_name)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)
