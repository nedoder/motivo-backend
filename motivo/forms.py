from django.contrib.auth.models import User
from django import forms
from .models import Attempt



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class AttemptForm(forms.ModelForm):
    class Meta:
        model = Attempt
        fields = ('user', 'challenge', 'file')


