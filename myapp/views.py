from django.shortcuts import render

# Create your views here.
def view1(request):
    return render(request,'myapp/view1.html')