from django.contrib.auth.models import Group
from django.core.exceptions import EmptyResultSet
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import GroupSerializer, UserSerializer, UserFullSerializer, UserCreateSerialize
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCreateSerialize


class UserLogin(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        login = self.request.data.get('username')
        user = User.objects.filter(username=login).first()
        if user and user.check_password(self.request.data.get('password')):
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Ошибка в email или пароле'}, status=status.HTTP_401_UNAUTHORIZED)


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserFullSerializer


class UserDetails(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
