from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import SubscriptionMealGroup, Subscription
from .serializers import SubscriptionMealGroupSerializer


class SubscriptionMealViewSet(ReadOnlyModelViewSet):
    serializer_class = SubscriptionMealGroupSerializer
    queryset = SubscriptionMealGroup.objects.all()

    def check_permissions(self, request):
        user = request.user
        try:
            subscription: Subscription = Subscription.objects.get(user=user)
            if not subscription.is_active:
                self.permission_denied(request, message='Subscription is not active')
        except Subscription.DoesNotExist:
            self.permission_denied(request, message='You are not subscribed')
        return super().check_permissions(request)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': 'Subscription Meal List fetched successfully',
            'data': serializer.data,
        })
