from django.shortcuts import render, redirect
from django.contrib.auth.forms import YourRegisterForm
from django.contrib.auth import login


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
