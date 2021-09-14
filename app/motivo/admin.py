from django.contrib import admin
from .models import Profile, Challenge, Attempt, Awards, CollectedAwards
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.admin.templatetags import admin_modify

admin.site.register(Profile)
admin.site.register(Challenge)
admin.site.register(Attempt)
admin.site.register(Awards)
admin.site.register(CollectedAwards)
admin.site.unregister(Group)

class UserAdmin(UserAdmin):

    list_display = ("username", "first_name", "last_name", "email")
    fieldsets = (
        (None, {'fields': ('username',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

submit_row = admin_modify.submit_row
def submit_row_custom(context):
    ctx = submit_row(context)
    ctx['show_save_and_add_another'] = False
    ctx['show_save_and_continue'] = False
    return ctx
admin_modify.submit_row = submit_row_custom


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "collected_coins", "collected_coins_gross", "initial_budget_gross", "annual_budget_gross")

admin.site.unregister(Profile)
admin.site.register(Profile, ProfileAdmin)

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "coins_to_win", "description")

admin.site.unregister(Challenge)
admin.site.register(Challenge, ChallengeAdmin)

class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "description", "challenge", "confirmed_by_admin")
    readonly_fields = ('user', 'description', 'challenge', 'file', 'date', 'number_of_attempts')

admin.site.unregister(Attempt)
admin.site.register(Attempt, AttemptAdmin)

class AwardsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price_in_coins")

admin.site.unregister(Awards)
admin.site.register(Awards, AwardsAdmin)

class CollectedAwardsAdmin(admin.ModelAdmin):
    list_display = ("awards", "user", "user_note")
    readonly_fields = ('awards','user', 'user_note')

admin.site.unregister(CollectedAwards)
admin.site.register(CollectedAwards, CollectedAwardsAdmin)


