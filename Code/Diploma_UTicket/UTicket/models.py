from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as __

from .managers import CustomUserManager
from uuid import uuid4

import secrets
import string


def generate_short_ticket_id(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# Create your models here.

class NewUser(AbstractUser):

    # Remove username field
    username = None

    ''' Add email field as unique identifiers
    for authentication instead of usernames '''
    email = models.EmailField(__("email address"), unique=True)

    # # Add d_o_b field
    # date_of_birth = models.DateField(null=True)

    # Assign an instance of a custom manager
    objects = CustomUserManager()

    # Declare fields
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email


class Tickets(models.Model):

    # Travel details
    city_of_departure = models.TextField()
    city_destination = models.TextField()
    departure_date = models.DateField()
    return_date = models.DateField()
    #amount_of_passengers = models.IntegerField()

    # Travel settings
    plane_class = models.TextField()
    flight_departure = models.TextField()
    plane_place = models.TextField()

    # Passenger data
    first_name = models.TextField()
    second_name = models.TextField()
    date_of_birth = models.TextField()
    phone_number = models.TextField()

    # Unique code
    ticket_number = models.CharField(max_length=10, unique=True, default=generate_short_ticket_id)


    # Connect tables
    email = models.ForeignKey(NewUser, on_delete=models.CASCADE)