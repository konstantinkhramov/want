from django.urls import path

from .. import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<int:pk>/', views.BookView.as_view(), name='book'),
    path('books/<int:pk>/chapters/', views.BookViewSet.as_view({'get': 'chapters', 'post': 'chapters'}), name='chapters'),
]
