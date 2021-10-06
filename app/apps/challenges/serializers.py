from .models import Challenge, ChallengeCategory, Attempt
from rest_framework import serializers

class ChallengeCategorySerializer(serializers.Serializer):
    class Meta:
        model = ChallengeCategory
        fields = '__all__'

class ChallengeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_challenge_icon')
    
    def get_challenge_icon(self, challenge):
        try:
            request = self.context.get("request")
            if request:
                return "https://" + request.get_host() + "/" + str(challenge.category.icon)
            raise Exception("")
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
