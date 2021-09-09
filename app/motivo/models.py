from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from model_utils import FieldTracker

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    collected_coins = models.IntegerField(default=0)
    initial_budget = models.IntegerField(default=0)
    annual_budget = models.IntegerField(default=0)

    def __str__(self):
        return 'Title: ' + str(self.title) + ', User: ' + str(self.user)  + ', Collected coins: ' + str(self.collected_coins)

class Challenge(models.Model):
    title = models.CharField(max_length=100, default='')
    coins_to_win = models.IntegerField(default=0)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)

    def __str__(self):
        return 'Title: ' + str(self.title) + ', Coins to win: ' + str(self.coins_to_win)

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, default=0)
    confirmed_by_admin = models.BooleanField(default=False)
    file = models.FileField(upload_to='uploads/attempts/', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    tracker = FieldTracker()

    def save(self, *args, **kwargs):
        profile = self.user.profile
        challenge = self.challenge
        print('-----------------')
        print(self.tracker.has_changed('confirmed_by_admin'))
        print(self.tracker.previous('confirmed_by_admin'))
        print('-----------------')
        if self.tracker.has_changed('confirmed_by_admin') and (self.tracker.previous('confirmed_by_admin')) is False:
            profile.collected_coins += challenge.coins_to_win
            profile.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "To be approved"

    def __str__(self):
        return 'User: ' + str(self.user) + ', Challenge: ' + str(self.challenge) + ', Confirmed by admin: ' + str(self.confirmed_by_admin)

class Awards(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, null=True, blank=True)
    price_in_coins = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)

    def __str__(self):
        return  'Title: ' + str(self.title) + ', Price in coins: ' + str(self.price_in_coins)

class CollectedAwards(models.Model):
    awards = models.ForeignKey(Awards, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)






