from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from model_utils import FieldTracker
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class ProfileManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Profile(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    title = models.CharField(max_length=100)
    collected_coins_gross = models.PositiveIntegerField(default=0)
    collected_coins = models.PositiveIntegerField(default=0)
    initial_budget_gross = models.PositiveIntegerField(verbose_name='Welcome pack budget', default=0)
    annual_budget_gross = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


CATEGORY_CHOICES = (
    ("Sport", "Sport"),
    ("Lifestyle", "Lifestyle"),
    ("Work", "Work"),
    ("Hobbies", "Hobbies"),
    ("Choice", "Choice")
)
class ChallengeCategory(models.Model):
    name = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Sport'
    )
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
    description = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='uploads/attempts/', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    number_of_attempts = models.CharField(
        max_length=20,
        choices=ATTEMPT_CHOICES,
        default='1'
    )
    def __str__(self):
        return  str(self.title)

class Attempt(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, default=0, related_name='attempts')
    confirmed_by_admin = models.BooleanField(default=False)
    file = models.FileField(upload_to='uploads/attempts/', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    tracker = FieldTracker()

    def save(self, *args, **kwargs):
        profile = self.user
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
        return  f"Challenge attempted by user {self.user}"


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
    price_in_coins = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    number_of_uses = models.CharField(
        max_length=20,
        choices=USED_CHOICES,
        default='1'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Awards"

class CollectedAwards(models.Model):
    awards = models.ForeignKey(Awards, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    user_note = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.awards)

    class Meta:
        verbose_name_plural = "Collected Awards"






