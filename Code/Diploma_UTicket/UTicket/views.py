from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def booking_page(request):
    return render(request, 'booking.html')

def cancel_page(request):
    return render(request, 'cancel-booking.html')

def check_page(request):
    return render(request, 'check-booking.html')