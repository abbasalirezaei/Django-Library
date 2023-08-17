from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class BookCategory(models.Model):
    category_name = models.CharField(max_length=255)
    created_date=models.DateTimeField(auto_now_add=True)
    max_books_per_customer = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.category_name


class Library(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

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


# from django.db.models.signals import pre_save
# from django.dispatch import receiver

# @receiver(pre_save, sender=Library)
# def check_max_books_borrowed(sender, instance, **kwargs):
#     # Check if the user has already borrowed the maximum number of books from the category
#     current_borrowed_count = Library.objects.filter(user=instance.user, category=instance.category).count()
#     if current_borrowed_count >= instance.max_books_borrowed:
#         raise Exception("You have reached the maximum limit for borrowing books from this category.")