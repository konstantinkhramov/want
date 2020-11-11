import requests
from django.contrib.auth.models import User
from django.urls import reverse
from oauth2_provider.models import Application
from oauthlib.uri_validate import scheme
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CreateUserSerializer

app_aouth = Application.objects.first()
if not app_aouth:
    admin = User.objects.filter(username='admin').first()
    app_aouth = Application(user=admin,
    client_type='confidential',
    authorization_grant_type='password',
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


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def token(request):
#     '''
#     Gets tokens with username and password. Input should be in the format:
#     {"username": "username", "password": "1234abcd"}
#     '''
#     r = requests.post(
#         f'http://localhost:8000/o/token/',
#         data={
#             'grant_type': 'password',
#             'username': request.data['username'],
#             'password': request.data['password'],
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#         },
#     )
#     return Response(r.json())


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def refresh_token(request):
#     '''
#     Registers user to the server. Input should be in the format:
#     {"refresh_token": "<token>"}
#     '''
#     r = requests.post(
#         f'http://localhost:8000/o/token/',
#         data={
#             'grant_type': 'refresh_token',
#             'refresh_token': request.data['refresh_token'],
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#         },
#     )
#     return Response(r.json())


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def revoke_token(request):
#     '''
#     Method to revoke tokens.
#     {"token": "<token>"}
#     '''
#     r = requests.post(
#         f'http://localhost:8000/o/revoke_token/',
#         data={
#             'token': request.data['token'],
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#         },
#     )
#     # If it goes well return sucess message (would be empty otherwise)
#     if r.status_code == requests.codes.ok:
#         return Response({'message': 'token revoked'}, r.status_code)
#     # Return the error if it goes badly
#     return Response(r.json(), r.status_code)
