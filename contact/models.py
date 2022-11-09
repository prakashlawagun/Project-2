from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.utils import Util
from account.models import User


# Create your models here.

class Profile(models.Model):
    class Membership(models.TextChoices):
        PREMINUM = 'PREMINUM', 'PREMINUM'
        FREE = 'FREE', 'FREE'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    is_preminum = models.CharField(max_length=10, choices=Membership.choices, default=Membership.FREE)


@receiver(post_save, sender=User)
def create_save_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


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
def send_reply(sender, **kwargs):
    rply_id = kwargs['instance']
    data = {
        'subject': 'Meal Time Family',
        'body': rply_id.msg,
        'to_email': rply_id.contact.email
    }
    Util.send_email(data)
