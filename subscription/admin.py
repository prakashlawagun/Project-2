from django.contrib import admin

from .models import Subscription, SubscriptionMealGroup


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'start_date', 'end_date', 'period', 'amount')
    list_filter = ('user', 'start_date', 'end_date')
    readonly_fields = ('end_date',)


@admin.register(SubscriptionMealGroup)
class SubscriptionMealGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal_group')
    list_filter = ('meal_group',)
