from django.urls import path,include

from .views import (
    borrowed_books,
    home,
    purchased_books
)

app_name='accounts'
urlpatterns = [
  
    path('dashboard/', home, name='dashboard'),
    path('borrowed/', borrowed_books, name='borrowed_books'),
    path('purchased/', purchased_books, name='purchased_books'),

]
