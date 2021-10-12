from django.contrib import admin
from .models import Profile, Challenge, Attempt, ChallengeCategory
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.admin.templatetags import admin_modify
from django.template.defaultfilters import mark_safe
from practice.settings import UPLOAD_FILE_MAX_SIZE_MB

admin.site.register(Challenge)
admin.site.register(Attempt)
admin.site.register(ChallengeCategory)

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "coins_to_win", "description", "number_of_attempts", "category", "file")

    def get_form(self, request, obj=None, **kwargs):
        form = super(ChallengeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['file'].label = mark_safe(f'File (Max-size {str(UPLOAD_FILE_MAX_SIZE_MB)}MB)')

        return form

admin.site.unregister(Challenge)
admin.site.register(Challenge, ChallengeAdmin)

class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "description", "challenge", "status")


    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('user', 'description', 'challenge', 'file', 'date')
        return self.readonly_fields
    #readonly_fields = ('user', 'description', 'challenge', 'file', 'date', 'number_of_attempts')

    def get_form(self, request, obj=None, **kwargs):
        form = super(AttemptAdmin, self).get_form(request, obj, **kwargs)
        # form.base_fields['confirmed_by_admin'].widget.attrs['style'] = 'filter: hue-rotate(240deg); transform: scale(2); margin:10px;'
        # form.base_fields['confirmed_by_admin'].label = mark_safe('<strong>Confirmed by admin</strong>')

        return form

admin.site.unregister(Attempt)
admin.site.register(Attempt, AttemptAdmin)

class ChallengeCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.unregister(ChallengeCategory)
admin.site.register(ChallengeCategory, ChallengeCategoryAdmin)

