from django.urls import path

from .. import views

urlpatterns = [
    path('chapters/<int:pk>/', views.ViewChapters.as_view(), name='chapter'),
]
