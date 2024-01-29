from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import NewUser
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

@login_required
def booking_page(request):
    return render(request, 'booking.html')

@login_required
def cancel_page(request):
    return render(request, 'cancel_booking.html')

@login_required
def check_page(request):
    return render(request, 'check_booking.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get("email")
        password = request.POST.get("password")
        date_of_birth = request.POST.get("date-of-birth")
        if first_name is None:
            return HttpResponse("<h3>Введите полное 1имя</h3>")
        elif last_name is None:
            return HttpResponse("<h3>Введите полное 2имя</h3>")
        elif email is None:
            return HttpResponse("<h3>Введите почту</h3>")
        elif password is None:
            return HttpResponse("<h3>Введите пароль</h3>")
        elif date_of_birth is None:
            return HttpResponse("<h3>Введите дату рождения</h3>")
        else:
            user = NewUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, )
            login(request, user)
            return redirect('index')
    return render(request, 'signup.html')


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
