from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    is_librarian = models.BooleanField(default=False)
    