from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    # date_of_birth = forms.DateField(label='Date of birth', widget=forms.DateInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

