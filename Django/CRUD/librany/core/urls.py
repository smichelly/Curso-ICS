from django.urls import path
from .views import book_create, book_list, book_update, book_delete

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/create/', book_create, name='book_create'),
    path('book/<int:pk>/update/', book_update, name='book_update'),
    path('book/<int:pk>/delete/', book_delete, name='book_delete'),
]