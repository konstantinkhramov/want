from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorView.as_view(), name='author')
]
