from rest_framework.serializers import ModelSerializer
from .models import Contact,Reply


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']


class ReplySerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = ['contact','msg']
