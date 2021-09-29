from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, ChallengeSerializer, CompletedSerializer, AttemptSerializer, UserEditSerializer, AwardsSerializer, PostAttemptSerializer, UserDataSerializer, CollectedAwardsSerializer, UsersCollectedAwardsSerializer
from .models import Profile, Challenge, Attempt, Awards, CollectedAwards
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from .tasks import Mailer
from django.db.models import Q, Count
import json
from django.http import JsonResponse
from django.core import serializers


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all().order_by('initial_budget_gross')
    serializer_class = UserSerializer

class UserDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = UserDataSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Profile.objects.filter(id=user.id)
        raise PermissionDenied()

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RankingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all().order_by('-collected_coins_gross')
    serializer_class = ProfileSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Challenge.objects.all().order_by('title')
    serializer_class = ChallengeSerializer

    def list(self, request):
        challenges = Challenge.objects.annotate(
            attempted_by_user=Count('attempts', filter=Q(attempts__user=request.user))) \
            .order_by('coins_to_win')
            
        # # counter = Attempt.objects.filter(challenge=challenges, user=request.user).count()
        # attempts_left = int(challenge.number_of_attempts) - counter
        # print(challenges)
        # print(challenges[0].attempted_by_user)
        challenges_data = []
        for challenge in challenges:
            challenge_obj = {
                "id": challenge.id,
                "title": challenge.title,
                "coins_to_win": challenge.coins_to_win,
                "description": challenge.description,
                "image": str(challenge.category.icon),
                "file": str(challenge.file),
                "attempted_by_user": challenge.attempted_by_user,
                "attempts_left": int(challenge.number_of_attempts) - challenge.attempted_by_user
            }
            challenges_data.append(challenge_obj)
        # challenges_json = json.dumps(challenges_data)
        return Response(challenges_data)

class CompletedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Attempt.objects.all().filter(confirmed_by_admin=True).order_by('date')
    serializer_class = CompletedSerializer


class AttemptViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Attempt.objects.all().filter(confirmed_by_admin=False)
    serializer_class = AttemptSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostAttemptSerializer(data=request.data)
        if serializer.is_valid():
            user = request.data.get("user")
            print('------')
            print(user)
            print('------')
            challenges = request.data.get("challenge")
            challenge = Challenge.objects.get(id=challenges)
            print('------')
            print(challenge.number_of_attempts)
            print('------')
            counter = Attempt.objects.filter(challenge=challenge, user=user).count()
            #counter = len(count)
            print('------')
            print('------')
            attempts_left = int(challenge.number_of_attempts) - counter
            if counter >= int(challenge.number_of_attempts):
                return Response({"message": "You reached the limit of attempts"}, status=status.HTTP_400_BAD_REQUEST)
            mail = Mailer()
            mail.send_messages(subject='Attempting the challenge',
                               context={'customer': self},
                               to_emails=['finalprojectreactnode@gmail.com'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEditViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = UserEditSerializer

class AwardsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

    def list(self, request):
        awards = Awards.objects.annotate(attempted_by_user=Count('collectedawards', filter=Q(collectedawards__user=request.user))).order_by('price_in_coins')
        print(awards)
        print(awards[0].attempted_by_user)
        awards_data = []
        for award in awards:
            awards_obj = {
                "id": award.id,
                "title": award.title,
                "price_in_coins": award.price_in_coins,
                "description": award.description,
                "image": str(award.image),
                "used": award.attempted_by_user,
                "awards_left": int(award.number_of_uses) - award.attempted_by_user
            }
            awards_data.append(awards_obj)
        # awards_json = json.dumps(awards_data)
        print(awards_data)
        return Response(awards_data)

class UsersAwardsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CollectedAwards.objects.all()
    serializer_class = UsersCollectedAwardsSerializer


class CollectedAwardsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CollectedAwards.objects.all()
    serializer_class = CollectedAwardsSerializer

    def create(self, request, *args, **kwargs):
        serializer = CollectedAwardsSerializer(data=request.data)
        if serializer.is_valid():
            user = request.data.get("user")
            print('------')
            print(user)
            print('------')
            profile = Profile.objects.get(id = user)
            awards = request.data.get("awards")
            award = Awards.objects.get(id = awards)
            print('------')
            print(award.number_of_uses)
            print('------')
            counter = CollectedAwards.objects.filter(awards=award, user= user).count()
            #counter = len(count)
            print('------')
            print('------')
            awards_left = int(award.number_of_uses) - counter
            if counter >= int(award.number_of_uses):
                return Response({"message": "You reached the limit of uses"}, status=status.HTTP_400_BAD_REQUEST)
            if profile.collected_coins >= award.price_in_coins:
                profile.collected_coins = profile.collected_coins - award.price_in_coins
                profile.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(awards)
        return Response({"message":"You have not enough coins"}, status=status.HTTP_400_BAD_REQUEST)

class DisplayImageView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, imagename):
        """
        Endpoint displays particular image.
        """
        image_path = f'uploads/images/{imagename}'
        image_data = open(image_path, "rb").read()
        
        return HttpResponse(image_data, content_type="image/*")