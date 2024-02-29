from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Quote, Author, Tag
from .forms import YourRegisterForm, AuthorForm, QuoteForm, TagSearchForm
from django.http import HttpResponse
from .forms import ScrapingForm
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView


def top_tags(request):
    top_tags = Tag.objects.order_by("-popularity")[:10]
    return render(request, "top_tags.html", {"top_tags": top_tags})


@login_required
def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, "registration/register.html", {"quotes": quotes})


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


def quotes_by_tag(request):
    if request.method == "POST":
        form = TagSearchForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data["tag_name"]
            tag = Tag.objects.get(name=tag_name)
            quotes = Quote.objects.filter(tags=tag)
    else:
        form = TagSearchForm()
        quotes = Quote.objects.all()

    return render(request, "quotes_by_tag.html", {"form": form, "quotes": quotes})


def home(request):
    # Получение всех цитат и сортировка по полю "id"
    all_quotes = Quote.objects.order_by("id")

    # Количество цитат на одной странице
    quotes_per_page = 10

    # Инициализация объекта Paginator
    paginator = Paginator(all_quotes, quotes_per_page)

    # Получение текущей страницы из параметра запроса или 1, если параметр не предоставлен
    page = request.GET.get("page", 1)

    try:
        # Получение объекта страницы
        current_page = paginator.page(page)
    except PageNotAnInteger:
        # Если номер страницы не является целым числом, получаем первую страницу
        current_page = paginator.page(1)
    except EmptyPage:
        # Если номер страницы находится за пределами допустимого диапазона, получаем последнюю страницу
        current_page = paginator.page(paginator.num_pages)

    return render(request, "home.html", {"current_page": current_page})


def scraping_view(request):
    if request.method == "POST":
        form = ScrapingForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            # Perform scraping logic here using requests and BeautifulSoup
            # Extract quotes and authors from the provided URL
            # Save the extracted data to the database
            # Redirect or render a response as needed
            return HttpResponse("Scraping completed successfully!")
    else:
        form = ScrapingForm()

    return render(request, "scraping.html", {"form": form})


class MyPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset_form.html"
    email_template_name = "registration/password_reset_email.html"
    subject_template_name = "registration/password_reset_subject.txt"


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"
