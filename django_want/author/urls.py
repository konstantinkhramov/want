from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='authors'),
]
