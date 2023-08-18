from django.shortcuts import render
from library.models import Library
from .utils import calculate_borrowing_days
from datetime import datetime, timedelta

# Create your views here.


def home(request):
    user=request.user
    return render(request,'accounts/index.html',{'user':'user'})



def borrowed_books(request):
    # Retrieve the books borrowed by the currently logged-in user
    borrowed_books = Library.objects.filter(customer_name=request.user)

    # print('------------------------------')
    # print(borrowed_books)
    # print('------------------------------')

    # borrowing_days = calculate_borrowing_days(
    #     borrowed_books.available_copies, 
    #     borrowed_books.id.borrowed_count_30_days
    #     )
    # borrowed_books.borrowing_days=borrowing_days

    context={ 
            
        'borrowed_books': borrowed_books,

        }
    return render(request, 'accounts/borrowed_books.html',
      context)



def purchased_books(request):
    purchased_books = Library.objects.filter(purchased_by=request.user)

    return render(request, 'accounts/purchased_books.html', {'purchased_books': purchased_books})

