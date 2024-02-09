from django.urls import path
from .views import (
    quote_list,
    SignUpView,
    home,
    author_list,
    add_author,
    add_quote,
    about,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", quote_list, name="quote_list"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path(
        "logout/", auth_views.LogoutView.as_view(), name="logout"
    ),  # Добавлен URL-путь для выхода
    path("signup/", SignUpView.as_view(), name="signup"),
    path("home/", home, name="home"),
    path("add_author/", add_author, name="add_author"),
    path("author_list/", author_list, name="author_list"),
    path("add_quote/", add_quote, name="add_quote"),
    path("about/", about, name="about"),
]
