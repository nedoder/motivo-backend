from rest_framework import serializers
from .models import Awards, CollectedAwards

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

