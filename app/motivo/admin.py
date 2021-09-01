
from django.contrib import admin
from .models import Profile, Challenge, Attempt, Awards, CollectedAwards


admin.site.register(Profile)
admin.site.register(Challenge)
admin.site.register(Attempt)
admin.site.register(Awards)
admin.site.register(CollectedAwards)



