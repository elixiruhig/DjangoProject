from django.shortcuts import render
#from googletrans import *
# Create your views here.
from googletrans import Translator


def transview(request):
    answer = ""
    if request.method == "POST" and 'translate' in request.POST:
        source = request.POST['source']
        translator = Translator()
        answer = translator.translate(source).text

    return render(request, "translate/transview.html", {"answer": answer})
