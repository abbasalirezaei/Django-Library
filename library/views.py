from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Library
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.utils import timezone

from .utils import calculate_borrowing_days


class BookListView(ListView):
    model=Library
    context_object_name='books'
    template_name='library/book_list.html'


def book_detail(request, pk):
    book=Library.objects.get(id=pk)
    borrowing_days = calculate_borrowing_days(book.available_copies, book.borrowed_count_30_days)
    book.borrowing_days=borrowing_days

    context= {
        'book': book,
        'borrowing_days':book.borrowing_days
    }
    return render(request, 'library/book_detail.html'  ,context)

def borrow_book(request, book_id):
    book = Library.objects.get(id=book_id)
   
    borrowing_days = calculate_borrowing_days(book.available_copies, book.borrowed_count_30_days)
    book.borrowing_days=borrowing_days
    
    return_date = book.borrowed_date + timedelta(days=borrowing_days)
    book.return_date=return_date
    
    if request.method == 'POST':
        # Check if the book is already borrowed
        # Perform the borrowing logic here
        # Update the book's availability and assign it to the currently logged-in user
        
        if book.customer_name == request.user:
            messages.success(request, 'You already borrowed this book.')
            return redirect('library:book-detail', pk=book_id)
            
            
        if book.customer_reached_category_limit(request.user):

            messages.error(request, 'you can\'t borrow this book because you reached category limit. ')
            return redirect('library:book-detail',pk=book_id)
        
 
       # Update the book's customer_name, borrowing_days, and borrowed_date fields
        
        if book.is_available ==True:
            book.is_available = False
            book.customer_name = request.user
            book.borrowing_days = borrowing_days
            book.borrowed_date = timezone.now()
            
            book.save()
            return redirect('library:book-detail',pk=book_id)
    return render(request, 'library/borrow_book.html', {'book': book,'borrowing_days':book.borrowing_days})





def buy_book(request, book_id):
    book = Library.objects.get(id=book_id)

    if request.method == 'POST':
        # Check if the book is already purchased by the user
        if request.user in book.purchased_by.all():
            return redirect('library:book-detail',pk=book_id)
            

        # Perform the buying logic here
        # Add the currently logged-in user to the purchased_by field
        book.purchased_by.add(request.user)

        return redirect('library:book-detail',pk=book_id)

    return render(request, 'library/buy_book.html', {'book': book})

