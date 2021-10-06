from django.db import models
from apps.motivo.models import Profile

# Create your models here.
class Awards(models.Model):
    USED_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
    )   

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
    user_note = models.CharField(max_length=100, default='', blank=True, null=True)

    def __str__(self):
        return str(self.awards)

    class Meta:
        verbose_name_plural = "Collected Awards"