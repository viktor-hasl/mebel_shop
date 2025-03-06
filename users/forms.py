from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'password1',
            'password2',
            'username',
            'first_name',
            'last_name',
            'email'
        )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'img',
            'username',
            'first_name',
            'last_name',
            'email'
        )