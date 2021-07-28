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

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.serializer_class(instance=instance, data=request.data, partial=True)
		if serializer.is_valid():
			self.object.set_password(serializer.data.get("password"))
			self.object.set_username(serializer.data.get("username"))
			self.object.set_email(serializer.data.get("email"))
			self.object.set_first_name(serializer.data.get("first_name"))
			self.object.set_last_name(serializer.data.get("last_name"))
			self.object.save()
		return Response(serializer.data, status=status.HTTP_200_OK)



