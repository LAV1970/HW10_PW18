from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    quote_list,
    SignUpView,
    home,
    author_list,
    add_author,
    add_quote,
    about,
    author_detail,
    quotes_by_tag,
    top_tags,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("quotes/", quote_list, name="quote_list"),
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
    path("author/<int:author_id>/", author_detail, name="author_detail"),
    path("quotes_by_tag/", quotes_by_tag, name="quotes_by_tag"),
    path("top_tags/", top_tags, name="top_tags"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
