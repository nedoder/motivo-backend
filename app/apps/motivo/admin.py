from django.contrib import admin
from .models import Profile
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.admin.templatetags import admin_modify
from django.template.defaultfilters import mark_safe
from practice.settings import UPLOAD_FILE_MAX_SIZE_MB

admin.site.register(Profile)
admin.site.unregister(Group)

submit_row = admin_modify.submit_row
def submit_row_custom(context):
    ctx = submit_row(context)
    ctx['show_save_and_add_another'] = False
    ctx['show_save_and_continue'] = False
    return ctx
admin_modify.submit_row = submit_row_custom

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

