import random
from .models import Quote
from django.shortcuts import render

# Create your views here.
def quoteview(request):
    rint = random.randint(0,1663)
    quote = Quote.objects.get(id = rint)
    quotes = []
    if request.method == 'POST' and 'Search' in request.POST:
        text = request.POST['searchbar']
        for str in Quote.objects.all():
            for string in str.quote.split():
                if text == string:
                    quotes.append(str.quote)
    return render(request,'quotes/quoteview.html',{'quote':quote.quote,'quotes':quotes})