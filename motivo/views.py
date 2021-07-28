from rest_framework import viewsets

from .serializers import UserSerializer, ProfileSerializer, ChallengeSerializer, CompletedSerializer, AttemptSerializer, UserEditSerializer
from .models import Profile, Challenge, Attempt
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
	queryset = Profile.objects.all().order_by('collected_coins')
	serializer_class = ProfileSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Challenge.objects.all().order_by('title')
	serializer_class = ChallengeSerializer

class CompletedViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Attempt.objects.all().filter(confirmed_by_admin=False).order_by('date')
	serializer_class = CompletedSerializer

class AttemptViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Attempt.objects.all()
	serializer_class = AttemptSerializer

class UserEditViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserEditSerializer

	def put(self, request):

		username = request.data['username']
		user = User.objects.get(username=username)
		serialized = UserEditSerializer(user, data=request.data)

		if serialized.is_valid():
			serialized.update(user, serialized.validated_data)
			return Response(data={"status": "api_user_update_ok"}, status=status.HTTP_201_CREATED)

		else:
			print(serialized.errors)
			return Response(data={"status": "api_user_update_failed", "error": serialized.errors.get('email')[0]},
							status=status.HTTP_400_BAD_REQUEST)



