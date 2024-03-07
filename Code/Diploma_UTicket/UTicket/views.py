from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import NewUser, Tickets
from django.contrib import messages
from django.contrib.auth import logout
#from uuid import uuid4
# Create your views here.


def home_page(request):
    return render(request, 'index.html')

@login_required
def booking_page(request):
    if request.method == "POST":
        city_of_departure = request.POST.get("city_of_departure")
        city_destination = request.POST.get("city_destination")
        departure_date = request.POST.get("departure_date")
        return_date = request.POST.get("return_date")
        #amount_of_passengers = request.POST.get("amount_of_passengers")

        # Travel settings
        plane_class = request.POST.get("plane_class")
        flight_departure = request.POST.get("flight_departure")
        plane_place = request.POST.get("plane_place")

        # Passenger data
        first_name = request.POST.get("first_name")
        second_name = request.POST.get("second_name")
        date_of_birth = request.POST.get("date_of_birth")
        phone_number = request.POST.get("phone_number")

        # Generate unique ticket
        #ticket_number = str(uuid4())

        # Connect tables
        #email = request.POST.get("email")


        if city_of_departure is None:
            return HttpResponse("<h3>Введіть city_of_departure</h3>")
        elif city_destination is None:
            return HttpResponse("<h3>Введіть city_destination</h3>")
        elif departure_date is None:
            return HttpResponse("<h3>Введіть departure_date</h3>")
        elif return_date is None:
            return HttpResponse("<h3>Введіть return_date</h3>")

        elif plane_class is None:
            return HttpResponse("<h3>Введіть plane_class</h3>")
        elif flight_departure is None:
            return HttpResponse("<h3>Введіть flight_departure/h3>")
        elif plane_place is None:
            return HttpResponse("<h3>Введіть plane_place</h3>")

        elif first_name is None:
            return HttpResponse("<h3>Введіть first_name</h3>")
        elif second_name is None:
            return HttpResponse("<h3>Введіть second_name</h3>")
        elif date_of_birth is None:
            return HttpResponse("<h3>Введіть date_of_birth</h3>")
        elif phone_number is None:
            return HttpResponse("<h3>Введіть phone_number</h3>")

        # elif ticket_number is None:
        #     return HttpResponse("<h3>Введіть ticketnumber</h3>")

        # elif email is None:
        #     return HttpResponse("<h3>Введіть email</h3>")


        else:
            user_instance = get_object_or_404(NewUser, email=request.user.email)

            ticket = Tickets.objects.create(city_of_departure=city_of_departure, city_destination=city_destination,
                                          departure_date=departure_date, return_date=return_date,
                                          plane_class=plane_class,
                                          flight_departure=flight_departure, plane_place=plane_place,
                                          first_name=first_name, second_name=second_name, date_of_birth=date_of_birth,
                                          phone_number=phone_number,  email=user_instance) #ticket_number=ticket_number,
            ticket.save()

            return redirect('index')
    return render(request, 'booking.html')


@login_required
def cancel_page(request):
    return render(request, 'cancel_booking.html')


@login_required
def check_page(request):
    if request.method == "POST":
        ticket_id = request.POST.get("ticket-id")

        if not ticket_id:
            return render(request, 'check_booking.html', {'error_message': 'Please provide a valid ticket ID.'})

        ticket = get_object_or_404(Tickets, ticket_number=ticket_id, email=request.user)

        return render(request, 'check_booking.html', {'ticket': ticket})

    return render(request, 'check_booking.html')


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
        date_of_birth = request.POST.get("date-of-birth")

        # Validate input fields
        if first_name is None:
            return HttpResponse("<h3>Введіть ім'я</h3>")
        elif last_name is None:
            return HttpResponse("<h3>Введіть прізвище</h3>")
        elif email is None:
            return HttpResponse("<h3>Введіть пошту</h3>")
        elif password is None:
            return HttpResponse("<h3>Введіть пароль</h3>")
        # elif date_of_birth is None:
        #     return HttpResponse("<h3>Введіть дату народження</h3>")
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



# @login_required
# def add_note(request):
#     if request.method == 'POST':
#         note_text = request.POST['note-text']
#         if note_text:
#             Note.objects.create(user=request.user, text=note_text)
#             return redirect('add_note')  # Возвращаемся на страницу добавления заметки
#     return render(request, 'add_note.html')  # Показываем страницу добавления заметки
#
# @login_required
# def notes(request):
#     user_notes = Note.objects.filter(user=request.user)
#     return render(request, 'notes.html', {'user_notes': user_notes})