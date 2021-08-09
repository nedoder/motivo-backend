from rest_framework import serializers
from .models import Profile, Challenge, Attempt
from django.contrib.auth.models import User
from practice.app.practice.celery import Mailer

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

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ('user', 'challenge', 'file' )

    def post(self, instance, validated_data):
        if validated_data.items():
            Mailer.send_messages(subject='My App account verification',
                   context={'customer': self},
                   to_emails=['nedoder89@gmail.com']);
        instance.save()
        return instance

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




