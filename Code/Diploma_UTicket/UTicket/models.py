from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class NewUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, )
    date_of_birth = models.DateField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']


