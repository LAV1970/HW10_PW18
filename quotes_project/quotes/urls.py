from django.urls import path
from .views import quote_list, SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", quote_list, name="quote_list"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),  # Добавили этот путь
]
