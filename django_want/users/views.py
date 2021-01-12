import requests
from django.contrib.auth.models import Group, User
from django.urls import reverse
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from oauth2_provider.contrib.rest_framework.permissions import TokenHasScope
from oauth2_provider.models import Application
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CreateUserSerializer, GroupSerializer, UserSerializer

app_aouth = Application.objects.first()
if not app_aouth:
    admin = User.objects.filter(username='admin').first()
    app_aouth = Application(user=admin,
                            client_type=Application.CLIENT_CONFIDENTIAL,
                            authorization_grant_type=Application.GRANT_PASSWORD,
                            name='django_want'
                            )
    app_aouth.save()

CLIENT_ID = app_aouth.client_id
CLIENT_SECRET = app_aouth.client_secret


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.create(serializer.validated_data)
        # Then we get a token for the created user.
        # This could be done differentley
        url_token = f"{request.scheme}://{request.get_host()}{reverse('oauth2_provider:token', current_app=request.resolver_match.namespace)}"
        try:
            r = requests.post(url_token,
                              data={
                                  'grant_type': 'password',
                                  'username': request.data['username'],
                                  'password': request.data['password'],
                                  'client_id': CLIENT_ID,
                                  'client_secret': CLIENT_SECRET,
                              },
                              )
        except requests.exceptions.ConnectionError:
            return Response({'error': 'Error connection'})

        return Response(r.json())
    return Response(serializer.errors)


class UserCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
