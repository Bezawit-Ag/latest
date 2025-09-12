from django.contrib import admin
from .models import Menu
from .models import Booking
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'guest_number', 'comment')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'Price')   

admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking, BookingAdmin)


# Register your models here.
