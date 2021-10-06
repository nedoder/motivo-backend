from django.contrib import admin
from .models import Awards, CollectedAwards

# Register your models here.
admin.site.register(Awards)
admin.site.register(CollectedAwards)

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
