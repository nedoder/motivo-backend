from rest_framework import serializers
from .models import Profile, Challenge, Attempt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'initial_budget', 'annual_budget', 'title')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'collected_coins')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('title', 'coins_to_win', 'description', 'image')

class CompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ('challenge', )







