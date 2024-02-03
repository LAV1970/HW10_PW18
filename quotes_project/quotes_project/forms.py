from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import User model


class YourRegisterForm(UserCreationForm):  # Rename the form to YourRegisterForm
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
