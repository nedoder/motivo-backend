from django.contrib import admin
from .models import AnnualBudgetStatistics, AnnualBudgetManagement

# Register your models here.
admin.site.register(AnnualBudgetStatistics)
admin.site.register(AnnualBudgetManagement)

class AnnualBudgetStatisticsAdmin(admin.ModelAdmin):
    list_display = ("user__first_name", "user__last_name", "user__email", "user__annual_budget_gross", "budget_left")
    
    def user__first_name(self, obj):
        return obj.user.first_name
    
    def user__last_name(self, obj):
        return obj.user.last_name
    
    def user__email(self, obj):
        return obj.user.email
    
    def user__annual_budget_gross(self, obj):
        return obj.user.annual_budget_gross

admin.site.unregister(AnnualBudgetStatistics)
admin.site.register(AnnualBudgetStatistics, AnnualBudgetStatisticsAdmin)


class AnnualBudgetManagementAdmin(admin.ModelAdmin):
    list_display = ("user__first_name", "user__last_name", "user__email", "title", "category", "when", "amount", "comment", "file", "status")

    def user__first_name(self, obj):
        return obj.user.first_name
    
    def user__last_name(self, obj):
        return obj.user.last_name
    
    def user__email(self, obj):
        return obj.user.email
    
    def user__title(self, obj):
        return obj.user.title
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('user', 'category', 'amount', 'comment', 'file')
        return self.readonly_fields
    
    
admin.site.unregister(AnnualBudgetManagement)
admin.site.register(AnnualBudgetManagement, AnnualBudgetManagementAdmin)