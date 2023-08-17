from django.urls import path,include

from .views import (BookListView,BookDetailView,borrow_book,borrowed_books,
buy_book,
purchased_books
)

app_name='library'
urlpatterns = [
  
    path('',BookListView.as_view(),name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:book_id>/borrow/', borrow_book, name='borrow_book'),
    path('books/borrowed/', borrowed_books, name='borrowed_books'),
    path('books/<int:book_id>/buy/', buy_book, name='buy_book'),
    path('books/purchased/', purchased_books, name='purchased_books'),

]
