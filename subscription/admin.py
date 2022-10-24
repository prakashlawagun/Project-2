from django.contrib import admin

from .models import Profile, Subscription, SubscriptionMealGroup


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'dob')
    list_filter = ('user', 'dob')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'start_date', 'end_date', 'period')
    list_filter = ('user', 'start_date', 'end_date')


@admin.register(SubscriptionMealGroup)
class SubscriptionMealGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal_group')
    list_filter = ('meal_group',)
