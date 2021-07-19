from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('initial_budget', 'annual_budget')