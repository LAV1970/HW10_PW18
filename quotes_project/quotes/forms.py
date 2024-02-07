from django.shortcuts import render, redirect
from django.contrib.auth.forms import YourRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.contrib.auth.models import User
from .models import Author


def register(request):
    if request.method == "POST":
        form = YourRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(
                "your-redirect-url"
            )  # Укажите URL для перенаправления после успешной регистрации
    else:
        form = YourRegisterForm()
    return render(request, "registration/register.html", {"form": form})


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]


class YourRegisterForm(UserCreationForm):
    # Добавьте поля формы и методы, если необходимо
    # Например:
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        # Ваша логика валидации для email
        pass
