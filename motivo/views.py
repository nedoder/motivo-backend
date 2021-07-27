from rest_framework import viewsets

from .serializers import UserSerializer, ProfileSerializer, ChallengeSerializer, CompletedSerializer
from .models import Profile, Challenge, Attempt

from .forms import UserForm
from django.shortcuts import render, redirect

from rest_framework.permissions import IsAuthenticated
from django.contrib import messages




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
	queryset = Attempt.objects.all().filter(confirmed_by_admin=False).order_by('title')
	serializer_class = CompletedSerializer



def userpage(request):
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		if user_form.is_valid():
			user_form.save()
			messages.success(request, ('Your user data was successfully updated!'))
		else:
			messages.error(request, ('Unable to complete request'))
		return redirect("user")
	user_form = UserForm(instance=request.user)
	return render(request=request, template_name="test.html", context={"user":request.user, "user_form":user_form })
