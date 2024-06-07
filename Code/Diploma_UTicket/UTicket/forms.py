from django import forms
from .models import Tickets
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['price', 'currency', 'description']

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['city_of_departure', 'city_destination', 'departure_date', 'return_date',
                  'flight_departure', 'flight_departure', 'plane_class', 'plane_place', 'first_name',
                  'second_name', 'date_of_birth', 'phone_number']
