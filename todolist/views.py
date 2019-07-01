from django.shortcuts import render, redirect
from .models import Category, Todolist
# Create your views here.
def todoview(request):
    todos = Todolist.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":

        if "taskAdd" in request.POST:

            name = request.POST['name']
            content = request.POST['content']
            created = request.POST['created']
            duedate = request.POST['duedate']
            category = request.POST['category_select']

            Todo = Todolist(name = name, content = content, created= created, duedate= duedate, category= Category.objects.get(name = category))
            Todo.save()
            return redirect("/todolist/")

        if "taskDelete"  in request.POST:
            deletelist = request.POST['checkedbox']

            for tid in deletelist:
                todo = Todolist.objects.get(id = int(tid))
                todo.delete()



    return render(request,'todolist/todoview.html',{"todos":todos, "categories":categories})

def editview(request,todo_id):
    if request.method == 'POST' and 'Update' in request.POST:
        obj = Todolist.objects.get(pk = todo_id)
        obj.name = request.POST['name']
        obj.content = request.POST['content']
        obj.created = request.POST['created']
        obj.duedate = request.POST['duedate']
        obj.category = Category.objects.get(name=request.POST['category_select'])
        obj.save()
        return render(request,'todolist/todoview.html',{'todos':Todolist.objects.all(),'categories':Category.objects.all()})

    return render(request,'todolist/edit.html',{'obj':Todolist.objects.get(pk=todo_id),'categories':Category.objects.all()})