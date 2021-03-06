from django.contrib import admin
from .models import Profile, Challenge, Attempt, Awards, CollectedAwards, ChallengeCategory
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.admin.templatetags import admin_modify
from django.template.defaultfilters import mark_safe
from practice.settings import UPLOAD_FILE_MAX_SIZE_MB

admin.site.register(Profile)
admin.site.register(Challenge)
admin.site.register(Attempt)
admin.site.register(Awards)
admin.site.register(CollectedAwards)
admin.site.register(ChallengeCategory)
admin.site.unregister(Group)

# class UserAdmin(UserAdmin):
#
#     list_display = ("username", "first_name", "last_name", "email")
#     fieldsets = (
#         (None, {'fields': ('username',)}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
#     )
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

submit_row = admin_modify.submit_row
def submit_row_custom(context):
    ctx = submit_row(context)
    ctx['show_save_and_add_another'] = False
    ctx['show_save_and_continue'] = False
    return ctx
admin_modify.submit_row = submit_row_custom


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ( "username","first_name", "last_name", "email", "title", "collected_coins", "collected_coins_gross", "initial_budget_gross", "annual_budget_gross")
#     fieldsets = (
#                 (None, {'fields': ('username',)}),
#                 (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'title', 'collected_coins', "collected_coins_gross", "initial_budget_gross", "annual_budget_gross")}),
#              )
# admin.site.unregister(Profile)
# admin.site.register(Profile, ProfileAdmin)


#admin.site.register(Profile)
class ProfileAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'title', 'collected_coins', "collected_coins_gross", "initial_budget_gross", "annual_budget_gross")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'title', "initial_budget_gross", "annual_budget_gross"),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', "title", "collected_coins", "collected_coins_gross", "initial_budget_gross", "annual_budget_gross")
    #search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.unregister(Profile)
admin.site.register(Profile, ProfileAdmin)

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "coins_to_win", "description", "number_of_attempts", "category", "file")

    def get_form(self, request, obj=None, **kwargs):
        form = super(ChallengeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['file'].label = mark_safe(f'File (Max-size {str(UPLOAD_FILE_MAX_SIZE_MB)}MB)')

        return form

admin.site.unregister(Challenge)
admin.site.register(Challenge, ChallengeAdmin)

class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "description", "challenge", "confirmed_by_admin")


    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('user', 'description', 'challenge', 'file', 'date')
        return self.readonly_fields
    #readonly_fields = ('user', 'description', 'challenge', 'file', 'date', 'number_of_attempts')

    def get_form(self, request, obj=None, **kwargs):
        form = super(AttemptAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['confirmed_by_admin'].widget.attrs['style'] = 'filter: hue-rotate(240deg); transform: scale(2); margin:10px;'
        form.base_fields['confirmed_by_admin'].label = mark_safe('<strong>Confirmed by admin</strong>')

        return form

admin.site.unregister(Attempt)
admin.site.register(Attempt, AttemptAdmin)

class AwardsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price_in_coins")

admin.site.unregister(Awards)
admin.site.register(Awards, AwardsAdmin)

class CollectedAwardsAdmin(admin.ModelAdmin):
    list_display = ("awards", "user", "user_note")

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('awards', 'user', 'user_note',)
        return self.readonly_fields
    #readonly_fields = ('awards','user', 'user_note')

admin.site.unregister(CollectedAwards)
admin.site.register(CollectedAwards, CollectedAwardsAdmin)

class ChallengeCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.unregister(ChallengeCategory)
admin.site.register(ChallengeCategory, ChallengeCategoryAdmin)



