from django.contrib import admin
from notification.models import UserNotification, Notification
from account.models import User

# Register your models here.
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def send_notification(self, request, queryset):
        notify = None
        try:
            notify = Notification.objects.latest('id')
            for user in queryset:
                UserNotification.objects.create(user=user, notify=notify)
            self.message_user(request, "Notification is sent to User.")
        except Notification.DoesNotExit:
            self.message_user(request, "No Notification available.")

    actions = ['send_notification']


admin.site.register([Notification, UserNotification])
