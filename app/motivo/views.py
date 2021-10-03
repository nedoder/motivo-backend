from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, ChallengeSerializer, CompletedSerializer, AttemptSerializer, UserEditSerializer, AwardsSerializer, PostAttemptSerializer, UserDataSerializer, CollectedAwardsSerializer, UsersCollectedAwardsSerializer, ChallengeCategorySerializer
from .models import ChallengeCategory, Profile, Challenge, Attempt, Awards, CollectedAwards
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

    def list(self, request):
        """Get user data after user is logging in"""
        user = request.user
        
        return Response({
            "id": user.id,
            "email": user.email,
            "title": user.title,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "collected_coins": user.collected_coins,
        }, status=status.HTTP_200_OK)

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
        # Retrieve challenges with amount of attempts taken by the user
        challenges = Challenge.objects.annotate(
            attempted_by_user=Count('attempts', filter=Q(attempts__user=request.user))) \
            .order_by('coins_to_win')
        
        # Prepare data to be properly formatted to read by frontend
        challenges_data = []
        for challenge in challenges:
            challenge_obj = {
                "id": challenge.id,
                "title": challenge.title,
                "coins_to_win": challenge.coins_to_win,
                "description": challenge.description,
                "image": "https://" + request.get_host() + "/" + str(challenge.category.icon),
                "category": challenge.category.name,
                "file": str(challenge.file),
                "attempted_by_user": challenge.attempted_by_user,   
                "attempts_left": int(challenge.number_of_attempts) - challenge.attempted_by_user
            }
            challenges_data.append(challenge_obj)
        # challenges_json = json.dumps(challenges_data)
        
        print(request.get_full_path())
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
            mail.send_messages(subject=f'Motivo - {request.user.first_name} {request.user.last_name} attempted the challenge {challenge.title}',
                               context=f"Hey!\n\n{request.user.first_name} {request.user.last_name} just attempted the challenge {challenge.title}.\nPlease review it in admin panel :)\n\nCheers, Motvo!",
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
        """
        Retrieve list of all the awards.
        Ordered by price_in_coins.
        
        """
        # Get all the awards
        awards = Awards.objects.annotate(attempted_by_user=Count('collectedawards', filter=Q(collectedawards__user=request.user))).order_by('price_in_coins')
        awards_data = []
        
        # Fill awards list with proper awards data
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
            counter = CollectedAwards.objects.filter(awards=awards, user= user).count()
            #counter = len(count)
            
            awards_left = int(award.number_of_uses) - counter
            if counter >= int(award.number_of_uses):
                return Response({"message": "You reached the limit of uses"}, status=status.HTTP_400_BAD_REQUEST)
            if profile.collected_coins >= award.price_in_coins:
                profile.collected_coins = profile.collected_coins - award.price_in_coins
                profile.save()
                serializer.save()
                
                # Send email notification to inform about the collected award
                mail = Mailer()
                mail.send_messages(subject='Motivo - award was collected',
                               context=f"Hey!\n\n{request.user.first_name} {request.user.last_name} wants to collect the award {award.title}.\n\nIncluded note:\n{serializer.data.get('user_note')}.\n\nCheers, Motivo!",
                               to_emails=['finalprojectreactnode@gmail.com'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(awards)
        return Response({"message":"You have not enough coins"}, status=status.HTTP_400_BAD_REQUEST)

class ChallengeCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ChallengeCategory.objects.all()
    serializer_class = ChallengeCategorySerializer
    
    def list(self, request):
        """Retrieve all the categories available in the system"""
        categories = list(ChallengeCategory.objects.all().order_by('name').values())
        for category in categories:
            category['icon'] = "https://" + request.get_host() + "/" + category['icon'],
        
        return Response(categories)


class DisplayImageView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, imagename):
        """
        Endpoint displays particular image.
        """
        image_path = f'uploads/images/{imagename}'
        image_data = open(image_path, "rb").read()
        
        return HttpResponse(image_data, content_type="image/*")