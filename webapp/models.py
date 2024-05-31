from django.db import models

class RandTool(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100, default='')
    description = models.TextField()
    category = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
    
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.BigIntegerField(default=1000000)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Visitor(models.Model):
    ip = models.GenericIPAddressField()
    points = models.BigIntegerField(default=1000000)