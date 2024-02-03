from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy(
        "login"
    )  
    # Укажите URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
