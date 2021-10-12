from django.db import models
from datetime import datetime
from model_utils import FieldTracker
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
import datetime

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
    budget_left_gross = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
    def save(self, *args, **kwargs):
        # If user is being created count the daily budget based on days left until the end of the year
        if self._state.adding:
            today = datetime.date.today()
            daily_budget = self.annual_budget_gross / 365
            days_until_end_of_the_year = (datetime.date(today.year, 12, 31) - today).days
            self.annual_budget_gross = daily_budget * days_until_end_of_the_year
            self.budget_left_gross = self.annual_budget_gross
        
        super(Profile, self).save(*args, **kwargs)
        
    def reset_annual_budget(self):
        """Reset annual budget that is left to initial value of annual budget"""
        self.budget_left_gross = self.annual_budget_gross
        self.save()
