from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'Price')   

admin.site.register(Menu, MenuAdmin)


# Register your models here.
