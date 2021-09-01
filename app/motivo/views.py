from rest_framework import viewsets

from .serializers import UserSerializer, ProfileSerializer, ChallengeSerializer, CompletedSerializer, AttemptSerializer, UserEditSerializer, AwardsSerializer, PostAttemptSerializer, UserDataSerializer, CollectedAwardsSerializer
from .models import Profile, Challenge, Attempt, Awards, CollectedAwards
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status



class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Profile.objects.all().order_by('initial_budget')
	serializer_class = UserSerializer

class UserDataViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserDataSerializer

	def get_queryset(self):
		user = self.request.user
		if user.is_authenticated:
			return User.objects.filter(id=user.id)
		raise PermissionDenied()

class ProfileViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class RankingViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Profile.objects.all().order_by('-collected_coins')
	serializer_class = UserSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Challenge.objects.all().order_by('title')
	serializer_class = ChallengeSerializer

class CompletedViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Attempt.objects.all().filter(confirmed_by_admin=True).order_by('date')
	serializer_class = CompletedSerializer


class AttemptViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Attempt.objects.all()
	serializer_class = AttemptSerializer

	def create(self, request, *args, **kwargs):
		serializer = PostAttemptSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEditViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserEditSerializer

class AwardsViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Awards.objects.all()
	serializer_class = AwardsSerializer


class CollectedAwardsViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = CollectedAwards.objects.all()
	serializer_class = CollectedAwardsSerializer

	# def create(self, request):
	# 	serializer = CollectedAwardsSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		user = request.data.user
	# 	# print(user)
	# 	# profile = Profile.objects.get(user.id=user)
	# 	# award_id = request.data.get('id')
	# 	# award = Awards.objects.get(id=award_id)
	# 	# print(award)
	# 		award = request.data.awards
	# 	# id = request.data['id']
	# 	# print(id)
	# 		if user.collected_coins >= award.price_in_coins:
	# 			return Response(date={'status': 'You got the award'}, status=status.HTTP_200_OK)
	# 		else:
	# 			print(serialized.errors)
	# 			return Response(date={'status': 'You dont have enough coins for this award',
	# 							  'error': serialized.errors.get(status=status.HTTP_400_BAD_REQUEST)})
