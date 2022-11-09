from django.contrib import admin
from .models import Contact, Reply


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'message']


@admin.register(Reply)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact','msg']
