from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Profile

class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    role=forms.ChoiceField(choices=[('agent','Agent'),('user','User')])
    class Meta:
        model = User
        fields = ['username','email','password']

class LoginForm(AuthenticationForm):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['phone','address','profile_image']
