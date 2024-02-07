from django.urls import path
from .views import quote_list, SignUpView, home
from django.contrib.auth import views as auth_views
from .views import author_list, add_author

urlpatterns = [
    path("", quote_list, name="quote_list"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("home/", home, name="home"),
    path("add_author/", add_author, name="add_author"),
    path("author_list/", author_list, name="author_list"),
]
