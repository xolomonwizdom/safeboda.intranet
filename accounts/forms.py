from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class RegistrationForm(UserCreationForm):
    team = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'team', 'password1', 'password2')
