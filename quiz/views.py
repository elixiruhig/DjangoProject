from django.http import HttpResponseRedirect, HttpResponse
from django.middleware import http
from django.shortcuts import render
from time import time
# Create your views here.
from quiz.models import Question


def quizview(request):
    objects = Question.objects.all()
    score = 0
    if request.method == 'POST' and 'submit' in request.POST:
        for i in objects:
           if request.POST[i.que].lower() == i.correct.lower():
                score = score + 1

    return render(request, 'quiz/quizview.html', {'objects': objects, 'score': score})