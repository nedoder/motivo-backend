from rest_framework import viewsets

from .serializers import UserSerializer, ProfileSerializer, ChallengeSerializer, CompletedSerializer, AttemptSerializer, UserEditSerializer, AwardsSerializer
from .models import Profile, Challenge, Attempt, Awards
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status



class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Profile.objects.all().order_by('initial_budget')
	serializer_class = UserSerializer

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

	def post(self, request):
		user_id = data.request.__getitem__('user_id')
		serializer = AttemptSerializer(user_id, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEditViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserEditSerializer

	def put(self, request):

		id = request.data['id']
		user = User.objects.get(id=id)
		serialized = UserEditSerializer(user, data=request.data)

		if serialized.is_valid():
			serialized.update(user, serialized.validated_data)
			return Response(data={"status": "api_user_update_ok"}, status=status.HTTP_200_OK)

		else:
			print(serialized.errors)
			return Response(data={"status": "api_user_update_failed", "error": serialized.errors.get('email')[0]},
							status=status.HTTP_400_BAD_REQUEST)


class AwardsViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Awards.objects.all()
	serializer_class = AwardsSerializer
