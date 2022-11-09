from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Contact, Reply
from .serializers import ContactSerializer, ReplySerializer
from account.utils import Util


# Create your views here.
class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ReplyViewSet(ModelViewSet):
    serializer_class = ReplySerializer

    def create(self, request, *args, **kwargs):
        serializer = ReplySerializer(data=request.data)

        reply = Reply.objects.create(
            message=serializer.validated_data['message'],
        )
        reply.save()
        # contact = Contact.objects.get_or_create(contact=request.data['contact'])
        # data = {
        #     'subject': 'Thank for your query',
        #     'body': reply.msg,
        #     'to_email': contact.email
        # }
        # Util.send_email(data)

        return Response({
            'msg': "Reply sent",
            'data': serializer.data
        })
