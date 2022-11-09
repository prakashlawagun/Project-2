from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.utils import Util


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = RichTextField()

    def __str__(self):
        return self.email


class Reply(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    msg = models.TextField(max_length=200)

    def __str__(self):
        return self.contact.email


@receiver(post_save, sender=Reply)
def send_reply(sender,**kwargs):
    rply_id = kwargs['instance']
    data = {
        'subject': 'Meal Time Family',
        'body': rply_id.msg,
        'to_email': rply_id.contact.email
    }
    Util.send_email(data)
