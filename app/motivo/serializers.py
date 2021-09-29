from rest_framework import serializers
from .models import Profile, Challenge, Attempt, Awards, CollectedAwards, ChallengeCategory


class UserSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    #
    # def get_user(self, obj):
    #     return {"username":obj.user.username, "id":obj.user.id}

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'initial_budget_gross', 'annual_budget_gross', 'title', 'collected_coins', 'collected_coins_gross')

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'email', 'username', )

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    # def get_user(self, obj):
    #     return {"username": obj.user.username, "id": obj.user.id, "first_name": obj.user.first_name, "last_name" : obj.user.last_name, "email":obj.user.email}
    class Meta:
        model = Profile
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'title', 'collected_coins', 'collected_coins_gross', 'initial_budget_gross', 'annual_budget_gross')

class ChallengeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_challenge_icon')
    
    def get_challenge_icon(self, challenge):
        try:
            return str(challenge.category.icon)
        except Exception as e:
            return ""

    
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'coins_to_win', 'description', 'image', 'file', 'category')

class CompletedSerializer(serializers.ModelSerializer):
    challenge = serializers.SerializerMethodField()

    def get_challenge(self, obj):
        return {"title":obj.challenge.title, "id":obj.challenge.id, "coins":obj.challenge.coins_to_win, "description":obj.challenge.description}


    class Meta:
        model = Attempt
        fields = ('challenge', )

class AttemptSerializer(serializers.ModelSerializer):
    challenge = serializers.SerializerMethodField()

    def get_challenge(self, obj):
        return {"title":obj.challenge.title, "id":obj.challenge.id, "coins":obj.challenge.coins_to_win, "description":obj.challenge.description }

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {"username":obj.user.username, "id":obj.user.id}

    class Meta:
        model = Attempt
        fields = ('user', 'challenge', 'file', 'description', 'confirmed_by_admin' )
        # depth = 1

class PostAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ('user', 'challenge', 'description', 'file', 'confirmed_by_admin')


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'password', 'email', 'username' )

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = ('id', 'title', 'description', 'price_in_coins', 'image', 'number_of_uses')

class CollectedAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedAwards
        fields = ('user', 'awards', 'user_note')


class UsersCollectedAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedAwards
        fields = ('user', 'awards')
        depth = 1

