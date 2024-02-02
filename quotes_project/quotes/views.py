from django.shortcuts import render
from .models import Quote


# Create your views here
def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, "quotes/quote_list.html", {"quotes": quotes})
