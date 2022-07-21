from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from notification.models import UserNotification, Notification
# from account.models import User


# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base  UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email','username','first_name','last_name','address','phone','tc','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','first_name','last_name','address','phone','tc',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','first_name','last_name','address','phone','tc','password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

    # def send_notification(self, request, queryset):
    #     notify = None
    #     try:
    #         notify = Notification.objects.latest('id')
    #         for user in queryset:
    #             UserNotification.objects.create(user=user, notify=notify)
    #         self.message_user(request, "Notification is sent to User.")
    #     except Notification.DoesNotExit:
    #         self.message_user(request, "No Notification available.")
    #
    # actions = ['send_notification']


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
# admin.site.register([Notification, UserNotification])