
from django.contrib import admin
from .models import Profile, Challenge, Attempt, Awards

# class MyAttemptAdmin(admin.ModelAdmin):
#
#     def save_model(self, request, obj, form, change):
#         obj.added_by = request.user
#         super().save_model(request, obj, form, change)
#         if obj.approved_by_admin is True:
#             profile.collected_coins += 1

admin.site.register(Profile)
admin.site.register(Challenge)
admin.site.register(Attempt)
admin.site.register(Awards)
# admin.site.register(MyAttemptAdmin)



