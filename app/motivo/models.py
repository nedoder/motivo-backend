from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from model_utils import FieldTracker

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    collected_coins_gross = models.IntegerField(default=0)
    collected_coins = models.IntegerField(default=0)
    initial_budget_gross = models.IntegerField(default=0)
    annual_budget_gross = models.IntegerField(default=0)

    def __str__(self):
        return 'Title: ' + str(self.title) + ', User: ' + str(self.user)  + ', Collected coins: ' + str(self.collected_coins)

class Challenge(models.Model):
    title = models.CharField(max_length=100, default='')
    coins_to_win = models.IntegerField(default=0)
    description = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='uploads/attempts/', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)

    def __str__(self):
        return 'Title: ' + str(self.title) + ', Coins to win: ' + str(self.coins_to_win)


ATTEMPT_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
)
class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, default=0)
    confirmed_by_admin = models.BooleanField(default=False)
    file = models.FileField(upload_to='uploads/attempts/', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    number_of_attempts = models.CharField(
        max_length=20,
        choices=ATTEMPT_CHOICES,
        default='1'
    )
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
            profile.collected_coins_gross += challenge.coins_to_win
            profile.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "To be approved"
        verbose_name_plural = "To be approved"

    def __str__(self):
        return 'User: ' + str(self.user) + ', Challenge: ' + str(self.challenge) + ', Confirmed by admin: ' + str(self.confirmed_by_admin)


USED_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
)
class Awards(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, null=True, blank=True)
    price_in_coins = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    number_of_uses = models.CharField(
        max_length=20,
        choices=USED_CHOICES,
        default='1'
    )

    def __str__(self):
        return  'Title: ' + str(self.title) + ', Price in coins: ' + str(self.price_in_coins)

    class Meta:
        verbose_name_plural = "Awards"

class CollectedAwards(models.Model):
    awards = models.ForeignKey(Awards, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    user_note = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Collected Awards"






