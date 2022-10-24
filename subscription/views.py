from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import SubscriptionMealGroup
from .serializers import SubscriptionMealGroupSerializer


class SubscriptionMealViewSet(ReadOnlyModelViewSet):
    serializer_class = SubscriptionMealGroupSerializer
    queryset = SubscriptionMealGroup.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': 'Subscription Meal List fetched successfully',
            'data': serializer.data,
        })
