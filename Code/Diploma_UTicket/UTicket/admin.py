from django.contrib import admin
from .models import NewUser, Tickets

# Register your models here.
admin.site.register(NewUser)
admin.site.register(Tickets)