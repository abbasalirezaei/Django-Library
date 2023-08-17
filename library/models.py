from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class BookCategory(models.Model):
    category_name = models.CharField(max_length=255)

    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name


class Library(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    created_date=models.DateTimeField(auto_now_add=True)    


    def __str__(self):
        return self.book_name