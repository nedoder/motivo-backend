from django.db import models
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
