from rest_framework import viewsets

from .serializers import UserSerializer
from .models import Profile

from .forms import UserForm, ProfileForm
from django.shortcuts import render, redirect

from rest_framework.permissions import IsAuthenticated

from django.contrib import messages

class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Profile.objects.all().order_by('initial_budget')
	serializer_class = UserSerializer

def userpage(request):
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid():
			user_form.save()
			messages.success(request, ('Your user data was successfully updated!'))
		elif profile_form.is_valid():
			profile_form.save()
			messages.success(request, ('Your profile was successfully updated!'))
		else:
			messages.error(request, ('Unable to complete request'))
		return redirect("userpage")
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="test.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })
