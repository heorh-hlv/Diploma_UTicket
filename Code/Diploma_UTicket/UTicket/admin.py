from django.contrib import admin
from .models import NewUser, Tickets, City, Departure


class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)


# Register your models here.
admin.site.register(NewUser)
admin.site.register(Tickets)
admin.site.register(City)
admin.site.register(Departure)