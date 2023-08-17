from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Library
from django.shortcuts import render, redirect

class BookListView(ListView):
    model=Library
    context_object_name='books'
    template_name='library/book_list.html'


class BookDetailView(DetailView):
    model = Library
    template_name = 'library/book_detail.html'  
    context_object_name = 'book' 



def borrow_book(request, book_id):
    book = Library.objects.get(id=book_id)


   
 
    if request.method == 'POST':
        # Check if the book is already borrowed
        # Perform the borrowing logic here
        # Update the book's availability and assign it to the currently logged-in user
        if book.customer_name == request.user:
            return redirect('library:book-detail', pk=book_id)
            
        if book.customer_reached_category_limit(request.user):
            return redirect('library:book-detail',pk=book_id)

        if book.is_available ==True:
            book.is_available = False
            book.customer_name = request.user
            book.save()
            return redirect('library:book-detail',pk=book_id)
        # return redirect('book_detail', book_id=book_id)

    return render(request, 'library/borrow_book.html', {'book': book})



def borrowed_books(request):
    # Retrieve the books borrowed by the currently logged-in user
    borrowed_books = Library.objects.filter(customer_name=request.user)

    return render(request, 'library/borrowed_books.html', {'borrowed_books': borrowed_books})




def buy_book(request, book_id):
    book = Library.objects.get(id=book_id)

    if request.method == 'POST':
        # Check if the book is already purchased by the user
        if request.user in book.purchased_by.all():
            return redirect('library:book_list')
            # return redirect('book_detail', book_id=book_id)

        # Perform the buying logic here
        # Add the currently logged-in user to the purchased_by field
        book.purchased_by.add(request.user)

        # return redirect('book_detail', book_id=book_id)
        return redirect('library:book_list')

    return render(request, 'library/buy_book.html', {'book': book})


def purchased_books(request):
    purchased_books = Library.objects.filter(purchased_by=request.user)

    return render(request, 'library/purchased_books.html', {'purchased_books': purchased_books})

