from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'initial_budget', 'annual_budget', 'title')




