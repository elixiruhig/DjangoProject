from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput

from tweet.models import UserProfile, Tweet


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)

    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('first_name','last_name','profile_pic' )

class TweetForm(forms.ModelForm):

    class Meta():
        model = Tweet
        fields = ('tweet','date','image')
