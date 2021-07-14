from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    initial_budget = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5000)])
    annual_budget = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5000)])

    def __str__(self):
        return self.first_name

