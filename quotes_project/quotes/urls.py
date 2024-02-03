from django.urls import path
from .views import quote_list

urlpatterns = [
    path("", quote_list, name="quote_list"),
]
