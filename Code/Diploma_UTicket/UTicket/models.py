from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as __
from .managers import CustomUserManager
import secrets
import string
from uuid import uuid4

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


class Tickets(models.Model):

    # Travel details
    city_of_departure = models.CharField(max_length=40)
    city_destination = models.CharField(max_length=40)
    departure_date = models.DateField()

    return_date = models.DateField(blank=True, null=True)
    # amount_of_passengers = models.IntegerField()

    # Travel settings
    plane_class = models.CharField(max_length=30)
    flight_departure = models.CharField(max_length=40)
    plane_place = models.CharField(max_length=30)

    # Passenger data
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    date_of_birth = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    # Unique code
    ticket_number = models.CharField(max_length=10, unique=True, default=generate_short_ticket_id)

    # Connect tables
    email = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    # Payment
    price = models.CharField(max_length=10)

    # Service
    transport_type = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client {self.first_name} {self.email} "


class Payment(models.Model):
    STATUS_CHOICES = [
        ('Оплата в процесі', 'Pending'),
        ('Підтверджено', 'Confirmed'),
        ('Відхилено', 'Failed'),
    ]

    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='UAH')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Оплата в процесі')
    token = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Payment {self.token} for ticket {self.ticket.email}"

