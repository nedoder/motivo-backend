from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, UserEditSerializer, UserDataSerializer
from .models import Profile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.db.models import Q, Count
import json
from django.core import serializers
from django.http import FileResponse, JsonResponse
import sys
from practice.tasks import challenge_mail, reward_mail

from apps.awards.models import Awards, CollectedAwards
from apps.awards.serializers import AwardsSerializer, CollectedAwardsSerializer, UsersCollectedAwardsSerializer
from apps.challenges.models import Challenge, ChallengeCategory, Attempt
from apps.challenges.serializers import PostAttemptSerializer, AttemptSerializer, CompletedSerializer, ChallengeSerializer, ChallengeCategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all().order_by('initial_budget_gross')
    serializer_class = UserSerializer
    
    def put(self, request):
        """Update password of the user"""
        password = request.data['password']
        repeat_password = request.data['repeat_password']
        
        if password != repeat_password:
            return Response({"message": "Repeated password is not the same"}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.set_password(password)
        request.user.save()
        return Response({"message":"Password changed successfully!"})

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
        
        category_filter = self.request.query_params.get('category_id')
        
        # Retrieve challenges with amount of attempts taken by the user
        counted_statuses = ["accepted", "waiting"]
        challenges = Challenge.objects.annotate(
            attempted_by_user=Count('attempts', filter=Q(attempts__user=request.user) & Q(attempts__status__in=counted_statuses))) \
            .order_by('coins_to_win') \
            .prefetch_related('category')
        
        # Filter challenges by the chosen category
        if category_filter and category_filter != "null" and category_filter != "undefined":
            challenges = challenges.filter(category__id=category_filter)
        
        # Divide challenges by active and non active
        active_challenges = []
        not_active_challenges = []
        
        for challenge in challenges:
            # Check if user attempted a challenge and is waiting for confirmation
            attempt_to_be_confirmed = Attempt.objects.filter(user=request.user, challenge=challenge, status="waiting").exists()
            challenge_available_to_attempt = False if attempt_to_be_confirmed else True
                
            challenge_obj = {
                "id": challenge.id,
                "title": challenge.title,
                "coins_to_win": challenge.coins_to_win,
                "description": challenge.description,
                "image": "https://" + request.get_host() + "/" + str(challenge.category.icon),
                "category": challenge.category.name,
                "file": str(challenge.file),
                "attempted_by_user": challenge.attempted_by_user,   
                "attempts_left": int(challenge.number_of_attempts) - challenge.attempted_by_user,
                "challenge_available_to_attempt": challenge_available_to_attempt
            }
            
            # Add challenge to proper list
            active_challenges.append(challenge_obj) if challenge_obj['attempts_left'] > 0 else not_active_challenges.append(challenge_obj)
        
        # challenges_json = json.dumps(challenges_data)
        
        # Sort challenges by coins
        active_challenges = sorted(active_challenges, key=lambda k: k['challenge_available_to_attempt'], reverse=True)
        not_active_challenges = sorted(not_active_challenges, key=lambda k: k['coins_to_win'], reverse=True)
        
        # Join challenges
        challenges_data = active_challenges + not_active_challenges
        
        return Response(challenges_data)

class CompletedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Attempt.objects.all().filter(status="accepted").order_by('date')
    serializer_class = CompletedSerializer


class AttemptViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Attempt.objects.all().filter(status="declined")
    serializer_class = AttemptSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostAttemptSerializer(data=request.data)
        if serializer.is_valid():
            user = request.data.get("user")

            challenges = request.data.get("challenge")
            challenge = Challenge.objects.get(id=challenges)

            attempts_statuses_to_count = ["waiting", "accepted"]
            counter = Attempt.objects.filter(challenge=challenge, user=user, status__in=attempts_statuses_to_count).count()
            #counter = len(count)

            attempts_left = int(challenge.number_of_attempts) - counter
            if not attempts_left:
                return Response({"message": "You reached the limit of attempts"}, status=status.HTTP_400_BAD_REQUEST)
            challenge_mail(request.user.first_name, request.user.last_name, challenge.title)
                 
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
            
        # Sort awards - put the ones not available at the end
        awards_data = sorted(awards_data, key=lambda x: x['awards_left'], reverse=True)

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
                reward_mail(request.user.first_name, request.user.last_name, award.title, serializer.data.get('user_note'))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            
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
        try:
            image_path = f'uploads/images/{imagename}'
            image_data = open(image_path, "rb").read()
        except Exception as e:
            print(f"There's no image in images/ --> {e}")
        
        try:
            image_path = f'uploads/attempts/{imagename}'
            image_data = open(image_path, "rb").read()
        except Exception as e:
            print(f"There's no image in attempts/ --> {e}'")
        
        return HttpResponse(image_data, content_type="image/*")
    
class DownloadFileView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, filename):
        # Get full path to file and open it
        full_path = request.get_full_path()[1:]
        return FileResponse(open(full_path, 'rb'), content_type='application/pdf')