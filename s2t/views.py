from django.shortcuts import render
import speech_recognition as sr
# Create your views here.
def s2tview(request):
    r = sr.Recognizer()
    if request.method == "POST" and 'submit' in request.POST:

        file = request.FILES.get('fileupload').url
        print(type(file))
        with sr.AudioFile(file) as source:
            audio = r.record(source)
        return render(request, "s2t/s2tview.html", {'text': r.recognize_google(audio)})
    return render(request, "s2t/s2tview.html")