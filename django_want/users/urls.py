from collections import UserList

from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.UserCreate.as_view(), name='user_create'),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<pk>/', views.UserDetails.as_view(), name='user'),
    path('group/', views.GroupList.as_view(), name='group')
]