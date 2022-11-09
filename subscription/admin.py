from django.contrib import admin

from .models import Profile, Subscription, SubscriptionMealGroup


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'dob', 'is_preminum')
    list_editable = ['is_preminum']
    list_filter = ('user', 'dob')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'start_date', 'end_date', 'period','amount')
    list_filter = ('user', 'start_date', 'end_date')
    readonly_fields = ('end_date',)


@admin.register(SubscriptionMealGroup)
class SubscriptionMealGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal_group')
    list_filter = ('meal_group',)


