from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


from django.core.management.base import BaseCommand
from django.utils import timezone

class BookCategory(models.Model):
    category_name = models.CharField(max_length=255)
    created_date=models.DateTimeField(auto_now_add=True)
    max_books_per_customer = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.category_name

from .utils import calculate_borrowing_days

class Library(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    available_copies = models.PositiveIntegerField(default=0)
    borrowed_count_30_days = models.PositiveIntegerField(default=0)

    borrowing_days = models.PositiveIntegerField(default=0)
    borrowed_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
  
    purchased_by = models.ManyToManyField(User, related_name='purchased_books', blank=True)
    customer_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)

    # created_date=models.DateTimeField(auto_now_add=True)    
   
    def customer_reached_category_limit(self, customer):
        # Check if the customer has reached the maximum limit for borrowing books from the category
        borrowed_books_from_category = Library.objects.filter(
            category=self.category,
            customer_name=customer
        ).count()
        return borrowed_books_from_category >= self.category.max_books_per_customer

    def __str__(self):
        return self.book_name


    def remaining_borrowing_days(self):
        if self.customer_name and self.borrowing_days > 0:
            now = timezone.now()
            expiration_date = self.borrowed_date + timezone.timedelta(days=self.borrowing_days)
            if now < expiration_date:
                return (expiration_date - now).days
        return 0