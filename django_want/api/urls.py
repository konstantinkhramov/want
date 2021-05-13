from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('users.urls')),
    path('', include('author.urls'))
]
