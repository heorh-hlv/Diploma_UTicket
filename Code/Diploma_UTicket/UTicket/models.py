from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as __
from .managers import CustomUserManager
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

    # Assign an instance of a custom manager
    objects = CustomUserManager()

    # Declare fields
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Departure(models.Model):

    departure_time = models.CharField(max_length=10)

    def __str__(self):
        return self.departure_time


class Tickets(models.Model):

    # Travel details
    city_of_departure = models.ForeignKey(City, related_name='departures', on_delete=models.CASCADE)
    city_destination = models.ForeignKey(City, related_name='destinations', on_delete=models.CASCADE)
    departure_date = models.DateField()

    # return_date = models.DateField()
    # amount_of_passengers = models.IntegerField()

    # Travel settings
    plane_class = models.TextField(max_length=30)
    flight_departure = models.ForeignKey(Departure, on_delete=models.CASCADE)
    plane_place = models.TextField(max_length=30)

    # Passenger data
    first_name = models.TextField(max_length=40)
    second_name = models.TextField(max_length=40)
    date_of_birth = models.TextField(max_length=10)
    phone_number = models.TextField(max_length=20)

    # Unique code
    ticket_number = models.CharField(max_length=10, unique=True, default=generate_short_ticket_id)


    # Connect tables
    email = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client {self.first_name} {self.email} "


# models.py
