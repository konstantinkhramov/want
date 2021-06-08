from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<int:pk>/', views.BookView.as_view(), name='book'),
    path('books/<int:pk>/chapters/', views.BookViewSet.as_view({'get': 'chapters', 'post': 'chapters'})),
    path('books/<int:pk>/chapters/<int:chapter_id>/', views.BookViewSet.as_view({'get': 'chapters'})),
    path('books/<int:pk>/parts/', views.BookViewSet.as_view({'get': 'parts', 'post': 'parts'})),
    path('books/<int:pk>/parts/<int:part_id>/', views.BookViewSet.as_view({'get': 'parts'}))

]
