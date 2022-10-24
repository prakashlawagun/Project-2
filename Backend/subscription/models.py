from django.db import models
from account.models import User
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver


# Create your models here.
class Packages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)


@receiver(post_save, sender=User)
def create_save_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

