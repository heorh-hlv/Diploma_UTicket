from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import NewUser, Tickets
from django.contrib import messages
from django.contrib.auth import logout
#from uuid import uuid4
# Create your views here.


def home_page(request):
    # if request.user.is_authenticated:
    #     try:
    #         ticket = Tickets.objects.get(email=request.user)
    #         ticket_number = ticket.ticket_number
    #     except Tickets.DoesNotExist:
    #         ticket_number = None
    # else:
    #     ticket_number = None
    #
    # context = {
    #     'ticket_number': ticket_number
    # }
    return render(request, 'index.html')


from .forms import BookingForm
@login_required(login_url='login_view')
def booking_page(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.email = request.user
            ticket.save()
            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})


@login_required(login_url='login_view')
def cancel_page(request):
    return render(request, 'cancel_booking.html')


@login_required(login_url='login_view')
def check_page(request):
    if request.method == "POST":
        ticket_number = request.POST.get("ticket_number")
        try:
            # Get the ticket object using the ticket_id
            tickets = Tickets.objects.filter(ticket_number=ticket_number)
            # Prepare data for the template
            context = {
                "tickets": tickets,
            }
            return render(request, "check_booking.html", context)
        except Tickets.DoesNotExist:
            # Handle case where ticket is not found
            context = {"error": "Ticket not found"}
            return render(request, "check_booking.html", context)
    else:
        return render(request, "check_booking.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Неверный адрес электронной почты или пароль.")
    return render(request, 'login.html')


def signup(request):

    # Check if the request method is POST
    if request.method == "POST":

        # Retrieve user input from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Validate input fields
        if first_name is None:
            return HttpResponse("<h3>Введіть ім'я</h3>")
        elif last_name is None:
            return HttpResponse("<h3>Введіть прізвище</h3>")
        elif email is None:
            return HttpResponse("<h3>Введіть пошту</h3>")
        elif password is None:
            return HttpResponse("<h3>Введіть пароль</h3>")
        else:

            # Create a new user using the NewUser model
            user = NewUser.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                               password=password) #, date_of_birth=date_of_birth

            # Log in the user after successful registration
            login(request, user)

            # Redirect to the index page
            return redirect('index')

    # If the request method is not POST, render the signup.html template
    return render(request, 'signup.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def change_user(request):
    logout(request)
    return redirect('login_view')

