from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import NewUser
from django.contrib.auth import logout
# Create your views here.
def home_page(request):
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

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST["email"]
#         password1, password2 = request.POST["password1"], request.POST["password2"]
#         if username is None:
#             return HttpResponse("<h3>Введите имя пользователя</h3>")
#         elif email is None:
#             return HttpResponse("<h3>Введите почту</h3>")
#         elif first_name is None:
#             return HttpResponse("<h3>Введите полное 1имя</h3>")
#         elif last_name is None:
#             return HttpResponse("<h3>Введите полное 2имя</h3>")
#         elif password1 is None or password2 is None:
#             return HttpResponse("<h3>Введите пароль</h3>")
#         elif password1 != password2:
#             return HttpResponse("<h3>Пароли должны совпадать</h3>")
#         else:
#             user = NewUser.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name)
#             login(request, user)
#             return redirect('home')
#     return render(request, 'reg.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#     return render(request, 'index.html')
#
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('index')