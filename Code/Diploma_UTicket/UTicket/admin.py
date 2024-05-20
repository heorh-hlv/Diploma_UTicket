from django.contrib import admin
from .models import NewUser, Tickets


class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)


# Register your models here.
admin.site.register(NewUser)
admin.site.register(Tickets)
