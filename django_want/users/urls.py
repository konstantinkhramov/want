from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('token/', views.token, name='token'),
    # path('token/refresh/', views.refresh_token, name='refresh_token'),
    # path('token/revoke/', views.revoke_token, name='revoke_token'),
]