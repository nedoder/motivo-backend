from django.db import models
from apps.motivo.models import Profile
from model_utils import FieldTracker

# Create your models here.
class AnnualBudgetStatistics(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    budget_left = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Budget stats for {self.user.first_name} {self.user.last_name}. Budget left: {self.budget_left}"
    
    class Meta:
        verbose_name = "Annual Budget Statistics"
        verbose_name_plural = "Annual Budget Statistics"
        
class AnnualBudgetManagement(models.Model):
    STATUSES = (
        ('accepted', 'accepted'),
        ('declined', 'declined'),
        ('waiting', 'waiting'),
    )
    
    CATEGORIES = (
        ('self-development', 'Self Development'),
        ('work-accessories', 'Work Accessories'),
        ('other','Other')
    )
    
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="budget_management")
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=64, choices=CATEGORIES, default="other")
    when = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/challenge_files/', null=True, blank=True)
    status = models.CharField(max_length=32, choices=STATUSES, default='waiting')
    tracker = FieldTracker()

    def __str__(self):
        return f"Budget management for {self.user.first_name} {self.user.last_name}. ({self.when.strftime('%d-%m-%Y')})"

    def save(self, *args, **kwargs):
        # If object is updated
        if not self._state.adding and self.tracker.has_changed('status'):
            if self.status == "declined":
                # If admin declines user request return the amount to users disposal
                self.user.budget_left_gross += self.amount
                self.user.save()
        
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Annual Budget Management"
        verbose_name_plural = "Annual Budget Management"