from django.shortcuts import render
import pyttsx3
# Create your views here.
def ttsview(request):
    if request.method == "POST":
        if "submit" in request.POST:
            txt = request.POST['txtinput']
            engine = pyttsx3.init()
            engine.setProperty('rate',150)
            engine.say(txt)
            engine.runAndWait()
    return render(request,"tts/ttsview.html")