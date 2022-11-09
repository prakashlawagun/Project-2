from django.contrib import admin
from .models import Contact, Reply,Profile


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'message']


@admin.register(Reply)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact','msg']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'dob', 'is_preminum')
    list_editable = ['is_preminum']
    list_filter = ('user', 'dob')
