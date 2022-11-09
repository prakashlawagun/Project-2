from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import SubscriptionMealGroup, Subscription
from .serializers import SubscriptionMealGroupSerializer, SubscriptionSerializer
from rest_framework.permissions import SAFE_METHODS
from contact.models import Profile


class SubscriptionMealViewSet(ReadOnlyModelViewSet):
    serializer_class = SubscriptionMealGroupSerializer
    queryset = SubscriptionMealGroup.objects.all()

    def check_permissions(self, request):
        user = request.user
        if request.method not in SAFE_METHODS:
            return True
        try:
            subscription: Subscription = Subscription.objects.get(user=user)
            if not subscription.is_active:
                self.permission_denied(request, "You are not active")
        except Subscription.DoesNotExist:
            self.permission_denied(request, "You are not Subscribe")
        return super().check_permissions(request)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': 'Subscription Meal List fetched successfully',
            'data': serializer.data,
        })

    def create(self, request, *args, **kwargs):
        serializer = SubscriptionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    'message': 'Invalid data',
                    'errors': serializer.errors,
                },
                status=400)
        if self.get_queryset().exists():
            new_sub = Subscription.objects.create(
                user=request.user,
                period=serializer.validated_data['period'],
                amount=0
            )
            new_sub.save()
            if new_sub.period == "Weekly":
                new_sub.amount = 10000
                new_sub.save()
            elif new_sub.period == "Monthly":
                new_sub.amount = 15000
                new_sub.save()
            elif new_sub.period == "Yearly":
                new_sub.amount = 20000
                new_sub.save()
            profile, _ = Profile.objects.get_or_create(user=request.user)
            profile.is_preminum = "PREMINUM"
            profile.save()
        else:
            return Response({
                'message': 'Package is empty,You cannot subscribe.'
            })
        return Response({
            'message': 'Subscription Created',
            'data': serializer.data,
        })



