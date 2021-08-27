from rest_framework import serializers
from .models import Profile, Challenge, Attempt
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Profile
        fields = ('user', 'initial_budget', 'annual_budget', 'title', 'collected_coins')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'collected_coins')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('title', 'coins_to_win', 'description', 'image')

class CompletedSerializer(serializers.ModelSerializer):
    challenge = serializers.SerializerMethodField()

    def get_challenge(self, obj):
        return obj.challenge.title


    class Meta:
        model = Attempt
        fields = ('challenge', )

class AttemptSerializer(serializers.ModelSerializer):
    challenge = serializers.SerializerMethodField()

    def get_challenge(self, obj):
        return obj.challenge.title

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Attempt
        fields = ('user', 'challenge', 'file', 'confirmed_by_admin' )

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'username' )

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance




