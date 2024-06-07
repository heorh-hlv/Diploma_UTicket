from django.contrib import admin
from .models import NewUser, Tickets, Payment


class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'price', 'status', 'token')
    list_filter = ('status',)
    search_fields = ('ticket__id', 'token')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == 'confirmed':
            return ['status']
        return []


# Register your models here.
admin.site.register(NewUser)
admin.site.register(Tickets)
admin.site.register(Payment)
