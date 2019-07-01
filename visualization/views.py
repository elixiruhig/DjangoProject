from django.shortcuts import render
from .models import Run
# Create your views here.
def chartview(request):
    steps = Run.objects.all()
    return render(request,"visualization/chartview.html",{'steps':steps})