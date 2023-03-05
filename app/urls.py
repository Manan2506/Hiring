from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('search/', views.search, name='search'),
]