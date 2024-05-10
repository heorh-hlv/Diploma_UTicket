from django import forms
from .models import Tickets

class BookingForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['city_of_departure', 'city_destination', 'departure_date', 'return_date', 'plane_class',
                  'flight_departure', 'plane_place', 'first_name', 'second_name', 'date_of_birth', 'phone_number']