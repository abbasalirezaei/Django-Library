from django.urls import path,include

from .views import (
    BookListView,
    book_detail,
    borrow_book,
    buy_book,
   
)

app_name='library'
urlpatterns = [
  
    path('',BookListView.as_view(),name='book_list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('books/<int:book_id>/borrow/', borrow_book, name='borrow_book'),
    path('books/<int:book_id>/buy/', buy_book, name='buy_book'),
    

]
