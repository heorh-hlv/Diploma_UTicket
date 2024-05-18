from django import forms
from .models import Tickets, City, Departure


class BookingForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['city_of_departure', 'city_destination', 'departure_date', 'plane_class',
                  'flight_departure', 'plane_place', 'first_name', 'second_name', 'date_of_birth', 'phone_number']

    city_of_departure = forms.ModelChoiceField(
        queryset=City.objects.all(),
        empty_label="Не обрано",
        label="Місто відправлення*"
    )

    city_destination = forms.ModelChoiceField(
        queryset=City.objects.all(),
        empty_label="Не обрано",
        label="Місто призначення*"
    )

    flight_departure = forms.ModelChoiceField(
        queryset=Departure.objects.all(),
        empty_label="Не обрано",
        label="Час відправлення*"
    )

