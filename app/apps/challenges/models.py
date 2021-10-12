from django.db import models
from datetime import datetime
from model_utils import FieldTracker
from django.utils.translation import ugettext_lazy as _
from .validators import validate_file_size
from apps.motivo.models import Profile

# Create your models here.
class ChallengeCategory(models.Model):
    CHALLENGE_CATEGORY_CHOICES = (
    ("Sport", "Sport"),
    ("Lifestyle", "Lifestyle"),
    ("Work", "Work"),
    ("Hobbies", "Hobbies"),
    ("Choice", "Choice")
    )
    
    name = models.CharField(max_length=64)
    
    # name = models.CharField(
    #     max_length=20,
    #     choices=CHALLENGE_CATEGORY_CHOICES,
    #     default='Sport'
    # )
    icon = models.ImageField(upload_to='uploads/images/', null=True, blank=True)

    class Meta:
        verbose_name = "Challenge category"
        verbose_name_plural = "Challenge category"

    def __str__(self):
        return  str(self.name)

ATTEMPT_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
)
class Challenge(models.Model):
    title = models.CharField(max_length=100, default='')
    coins_to_win = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ChallengeCategory, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/challenge_files/', null=True, blank=True, validators=[validate_file_size])
    # image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    number_of_attempts = models.CharField(
        max_length=20,
        choices=ATTEMPT_CHOICES,
        default='1'
    )
    def __str__(self):
        return  str(self.title)

class Attempt(models.Model):
    STATUSES = (
        ('accepted', 'accepted'),
        ('declined', 'declined'),
        ('waiting', 'waiting'),
    )
    
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, default=0, related_name='attempts')
    # confirmed_by_admin = models.BooleanField(default=False)
    file = models.FileField(upload_to='uploads/attempts/', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=32, choices=STATUSES, default='waiting')
    tracker = FieldTracker()

    def save(self, *args, **kwargs):
        profile = self.user
        challenge = self.challenge
        # if self.tracker.has_changed('confirmed_by_admin') and (self.tracker.previous('confirmed_by_admin')) is False:
        #     profile.collected_coins += challenge.coins_to_win
        #     profile.collected_coins_gross += challenge.coins_to_win
        #     profile.save()
            
        if self.tracker.has_changed('status'):
            if self.status == "accepted":
                print(self.tracker.previous('status'))
                profile.collected_coins += challenge.coins_to_win
                profile.collected_coins_gross += challenge.coins_to_win
                profile.save()
            elif self.status == "declined":
                if self.tracker.previous('status') == "accepted":
                    profile.collected_coins -= challenge.coins_to_win
                    profile.collected_coins_gross -= challenge.coins_to_win
                    profile.save()
                    
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "To be approved"
        verbose_name_plural = "To be approved"

    def __str__(self):
        return  f"Challenge attempted by user {self.user}"
