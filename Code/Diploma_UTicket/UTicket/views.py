from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import NewUser, Tickets, Payment
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookingForm, PaymentForm
from django.template.loader import render_to_string
import random

# Create your views here.


def home_page(request):
    return render(request, 'index.html')


@login_required(login_url='login_view')
def choose_booking(request):
    return render(request, 'choose_booking.html')


# @login_required(login_url='login_view')
# def booking_train(request):
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             ticket = form.save(commit=False)
#
#             user = NewUser.objects.get(email=request.user.email)
#
#             ticket.email = user
#
#             ticket.save()
#             print("Success")
#             send_booking_email(ticket)
#
#             return redirect('index')
#         else:
#             print("Form is not valid")
#             print(form.errors)
#     else:
#         form = BookingForm()
#     return render(request, 'booking_train.html', {'form': form})
#
#
# @login_required(login_url='login_view')
# def booking_plane(request):
#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             ticket = form.save(commit=False)
#
#             user = NewUser.objects.get(email=request.user.email)
#
#             ticket.email = user
#
#             ticket.save()
#             print("Success")
#             send_booking_email(ticket)
#
#             return redirect('index')
#         else:
#             print("Form is not valid")
#             print(form.errors)
#     else:
#         form = BookingForm()
#     return render(request, 'booking_plane.html', {'form': form})


def send_booking_email(ticket):
    subject = 'Успішна покупка'
    email_template_name = 'email_confirmation.html'
    context = {'ticket': ticket}

    email_html_message = render_to_string(email_template_name, context)

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ticket.email, ]
    send_mail(subject, '', email_from, recipient_list, html_message=email_html_message)


def choose_seat(transport_class, transport_place):
    if transport_class in ('Сидячий першого класу', 'Сидячий другого класу'):
        if transport_class == 'Сидячий першого класу':
            car_number = random.choice(range(1, 6))  # First 5 cars
        elif transport_class == 'Сидячий другого класу':
            car_number = random.choice(range(6, 25))  # Remaining 19 cars

        # Define seat number and type
        transport_place = random.randint(1, 50)  # 50 seats per car
        if transport_place == "У вікна":
            seat_label = f"{transport_place}B"
        elif transport_place == "У проходу":
            seat_label = f"{transport_place}A"
        else:
            seat_label = f"{transport_place}{random.choice(['A', 'B'])}"

        return f"Вагон №{car_number}, місце {seat_label}"

    else:
        # AirbusA380:
        #
        # Общееколичество мест: 525
        # Эконом - класс: 400 - 600мест
        # Бизнес - класс: 50 - 100мест
        # Первый класс: 10 - 20 мест

        if transport_class == 'Стандарт':
            seat_number = random.randint(1, 400)
        elif transport_class == 'Бізнес':
            seat_number = random.randint(401, 500)
        elif transport_class == 'Перший':
            seat_number = random.randint(501, 525)

        if transport_place == "У вікна":
            seat_label = f"{seat_number}C"
        elif transport_place == "У проходу":
            seat_label = f"{seat_number}A"
        else:
            seat_label = f"{seat_number}{random.choice(['A', 'B', 'C'])}"

        return seat_label


def calculate_price(city_departure, city_destination, transport_class):
    price = 0

    ukraine = ['Київ', 'Харків', 'Дніпро', 'Львів']
    east_europe = ['Варшава', 'Прага', 'Будапешт', 'Бухарест']
    west_europe = ['Берлін', 'Париж', 'Лондон', 'Мадрид']

    # City price
    if city_departure in ukraine:
        if city_destination in ukraine:
            price += 20
        elif city_destination in east_europe:
            price += 30
        elif city_destination in west_europe:
            price += 40
    elif city_departure in east_europe:
        if city_destination in ukraine:
            price += 25
        elif city_destination in east_europe:
            price += 20
        elif city_destination in west_europe:
            price += 35
    elif city_departure in west_europe:
        if city_destination in ukraine:
            price += 40
        elif city_destination in east_europe:
            price += 35
        elif city_destination in west_europe:
            price += 20

    # Transport class price
    if transport_class == 'Сидячий першого класу':
        price += 15
    elif transport_class == 'Бізнес':
        price += 15
    elif transport_class == 'Перший':
        price += 25

    return price


@login_required(login_url='login_view')
def booking(request, transport, travel_type):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            user = NewUser.objects.get(email=request.user.email)
            ticket.email = user
            ticket.plane_place = choose_seat(ticket.plane_class, ticket.plane_place)
            ticket.price = calculate_price(ticket.city_of_departure, ticket.city_destination,
                                           ticket.plane_class)
            ticket.save()
            send_booking_email(ticket)
            return redirect('process_payment', ticket_id=ticket.id)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = BookingForm()

    template_name = 'booking_plane.html'
    if transport == 'train':
        template_name = 'booking_train.html'
    if travel_type == 'roundtrip':
        template_name = template_name.replace('.html', '_roundtrip.html')

    return render(request, template_name, {'form': form})


@login_required(login_url='login_view')
def process_payment(request, ticket_id):
    ticket = get_object_or_404(Tickets, id=ticket_id)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.ticket = ticket
            payment.price = ticket.price
            payment.save()
            return redirect('payment_done', token=payment.token)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = PaymentForm(initial={
            'price': ticket.price,
            'currency': 'UAH',
            'description': f'Оплата для білету {ticket.ticket_number}',
        })
    return render(request, 'payment.html', {'form': form, 'ticket': ticket})


@login_required(login_url='login_view')
def payment_done(request, token):
    payment = get_object_or_404(Payment, token=token)
    return render(request, 'payment_done.html', {'payment': payment})


@login_required(login_url='login_view')
def cancel_page(request):
    return render(request, 'cancel_booking.html')


@login_required(login_url='login_view')
def check_page(request):
    if request.method == "POST":
        ticket_number = request.POST.get("ticket_number")
        if ticket_number:
            tickets = Tickets.objects.filter(ticket_number=ticket_number)
            if tickets.exists():
                for ticket in tickets:
                    payment = Payment.objects.filter(ticket=ticket).first()
                    ticket.payment_status = payment.status if payment else "No Payment Info"

                return render(request, "check_booking.html", {"tickets": tickets})
            else:
                return render(request, "check_booking.html", {"error": "Білет не знайдено"})
        else:
            return render(request, "check_booking.html", {"error": "Будь ласка, введіть номер квитка"})
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
            messages.error(request, "Неправильна пошта або пароль.")
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":

        # retrieve user input from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get("email")
        password = request.POST.get("password")

        # validate input fields
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
                                               password=password)

            # Log in the user after successful registration
            login(request, user)

            # Redirect to the index page
            return redirect('index')

    # If the request method is not POST, render the signup.html template
    return render(request, 'signup.html')


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login_view')
def change_user(request):
    logout(request)
    return redirect('login_view')


