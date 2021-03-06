__author__ = 'rafael'

from django import forms

from base.models import UserProfile, User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


# d

class UserProfileForm(forms.ModelForm):
    city = forms.CharField(max_length=100, help_text="Please enter your current location")

    class Meta:
        model = UserProfile
        fields = ('city', 'picture')