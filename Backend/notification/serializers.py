from notification.models import UserNotification
from rest_framework import serializers


class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = ['id','notify', 'created_at', 'seen_by']
        depth = 1

        def get_queryset(self):
            return UserNotification.objects.filter(user=self['request'].user)

