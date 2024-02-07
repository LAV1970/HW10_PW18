from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Quote, Author
from .forms import YourRegisterForm, AuthorForm


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, "quotes/quote_list.html", {"quotes": quotes})


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"  # Изменено здесь
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("quote_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def home(request):
    return render(request, "home.html")


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(
                "author_list"
            )  # Предположим, что у вас есть представление для вывода списка авторов
    else:
        form = AuthorForm()
    return render(request, "add_author.html", {"form": form})
