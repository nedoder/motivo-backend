from rest_framework import viewsets

from .serializers import UserSerializer
from .models import Profile

from .forms import NewUserForm, UserForm, ProfileForm
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = Profile.objects.all().order_by('initial_budget')
	serializer_class = UserSerializer

def userpage(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="test.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })
