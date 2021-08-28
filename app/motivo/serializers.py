from rest_framework import serializers
from .models import Profile, Challenge, Attempt, Awards
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {"username":obj.user.username, "id":obj.user.id}

    class Meta:
        model = Profile
        fields = ('user', 'initial_budget', 'annual_budget', 'title', 'collected_coins')

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {"username": obj.user.username, "id": obj.user.id, "first_name": obj.user.first_name, "last_name" : obj.user.last_name, "email":obj.user.email}
    class Meta:
        model = Profile
        fields = ('user', 'title', 'collected_coins', 'initial_budget', 'annual_budget')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'coins_to_win', 'description', 'image')

class CompletedSerializer(serializers.ModelSerializer):
    challenge = serializers.SerializerMethodField()

    def get_challenge(self, obj):
        return {"title":obj.challenge.title, "id":obj.challenge.id}


    class Meta:
        model = Attempt
        fields = ('challenge', )

class AttemptSerializer(serializers.ModelSerializer):
    challenge = serializers.SerializerMethodField()

    def get_challenge(self, obj):
        return {"title":obj.challenge.title, "id":obj.challenge.id}

    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {"username":obj.user.username, "id":obj.user.id}

    class Meta:
        model = Attempt
        fields = ('user', 'challenge', 'file', 'confirmed_by_admin' )

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'username' )

    # def update(self, instance, validated_data):
    #     for attr, value in validated_data.items():
    #         if attr == 'password':
    #             instance.set_password(value)
    #         else:
    #             setattr(instance, attr, value)
    #     instance.save()
    #     return instance

    def put(self,required):
        id = request.data['id']
        user = User.objects.get(id=id)
        serialized = UserEditSerializer(user, data = request.data)

        if serialized.is_valid():
            serialized.update(user, serialized.validated_data)
            return Response(date={'status':'api user update ok'}, status=status.HTTP_200_OK)
        else:
            print(serialized.errors)
            return Response(date={'status': 'api user update failed', 'error': serialized.errors.get(status=status.HTTP_400_BAD_REQUEST)})


class AwardsSerializer(serializers.ModelSerializer):
    challenge = serializers.SerializerMethodField()

    def get_challenge(self, obj):
        return {"title":obj.challenge.title, "id":obj.challenge.id}


    class Meta:
        model = Awards
        fields = ('challenge', 'title', 'description', 'price_in_coins', 'image' )

