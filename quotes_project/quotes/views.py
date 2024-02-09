from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Quote, Author
from .forms import YourRegisterForm, AuthorForm, QuoteForm


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, "registration/register.html")


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


def author_list(request):
    # Получаем все объекты Author из базы данных
    authors = Author.objects.all()

    # Передаем список авторов в контекст шаблона
    context = {"authors": authors}
    return render(request, "author_list.html", {})


def add_quote(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = QuoteForm(request.POST)
            if form.is_valid():
                quote = form.save(commit=False)
                quote.user = request.user
                quote.save()
                return redirect("quote_list")
        else:
            form = QuoteForm()
        return render(request, "quotes/add_quote.html", {"form": form})
    else:
        return redirect("login")


def about(request):
    form = QuoteForm()  # Определите переменную формы
    return render(request, "quotes/add_quote.html", {"form": form})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, "author_detail.html", {"author": author})
