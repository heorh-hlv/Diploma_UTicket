from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import NewUser
from django.contrib.auth import logout
# Create your views here.
def index_page(request):
    return render(request, 'index.html')
#@login_required
def booking_page(request):
    return render(request, 'booking.html')
#@login_required
def cancel_page(request):
    return render(request, 'cancel_booking.html')
#@login_required
def check_page(request):
    return render(request, 'check_booking.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST["email"]
        password = request.POST["password"]
        if email is None:
            return HttpResponse("<h3>Введите почту</h3>")
        elif first_name is None:
            return HttpResponse("<h3>Введите полное 1имя</h3>")
        elif last_name is None:
            return HttpResponse("<h3>Введите полное 2имя</h3>")
        elif password is None:
            return HttpResponse("<h3>Введите пароль</h3>")
        else:
            user = NewUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect('index.html')
    return render(request, 'signup.html')
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')