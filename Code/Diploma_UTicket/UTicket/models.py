from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
# Create your models here.

class NewUser(AbstractUser):
    username = None

    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email




