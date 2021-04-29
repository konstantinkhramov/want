from collections import UserList

from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<pk>/', views.UserDetails.as_view(), name='user'),
    path('group/', views.GroupList.as_view(), name='group')
]