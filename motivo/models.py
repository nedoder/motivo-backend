from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    initial_budget = models.IntegerField(validators=[MinValueValidator(0),
                                                     MaxValueValidator(5000)], null=True)
    annual_budget = models.IntegerField(validators=[MinValueValidator(0),
                                                    MaxValueValidator(5000)], null=True)
class Challenge(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    coins_to_win = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=True, blank=True, default=0)
    confirmed_by_admin = models.BooleanField(default=False, null=True, blank=True)
    file = models.FileField(upload_to='uploads/attempts/', null=True, blank=True)





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

