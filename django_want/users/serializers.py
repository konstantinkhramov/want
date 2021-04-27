from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username,
                                        password=password)
        token = Token.objects.create(user=user)
        token.save()
        user.token = token.key
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'token')


class UserCreateSerialize(UserSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)
