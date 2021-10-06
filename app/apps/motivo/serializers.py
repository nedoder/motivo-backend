from rest_framework import serializers
from .models import Profile

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
