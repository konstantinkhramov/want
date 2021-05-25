from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<int:pk>/', views.BookView.as_view(), name='book')
]
