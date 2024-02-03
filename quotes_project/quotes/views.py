from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import YourRegisterForm  # Update import to use YourRegisterForm


def register(request):
    if request.method == "POST":
        form = YourRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("your-redirect-url")
    else:
        form = YourRegisterForm()
    return render(request, "registration/register.html", {"form": form})
