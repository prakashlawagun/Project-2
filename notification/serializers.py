from notification.models import UserNotification,Notification
from rest_framework import serializers


class UserNotificationSerializer(serializers.ModelSerializer):
    seen_by = serializers.BooleanField(default=False)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        items_count = Notification.objects.all().count()
        response['count'] = items_count
        return response

    class Meta:
        model = UserNotification
        fields = ['id', 'notify', 'created_at', 'seen_by']
        depth = 1

        def get_queryset(self):
            return UserNotification.objects.filter(user=self['request'].user)


