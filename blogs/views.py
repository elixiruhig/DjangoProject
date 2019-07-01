from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from blogs.forms import UserForm, UserProfileForm
from blogs.models import Post


# Create your views here.
def blogview(request):
    posts = Post.objects.all()
    return render(request,'blogs/blogview.html',{'posts' : posts})

def postdetail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,"blogs/postdetail.html",{'post':post})

def user_login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('blogs:blogview')
            else:
                return HttpResponse("Account inactive")
        else:
            print("Failed login using username : {} and password : {}".format(username,password))
            return HttpResponse('Invalid details')
    else:
        return render(request,'blogs/login.html')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()


            return render(request,'blogs/blogview.html')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        context = {'user_form':user_form,'profile_form':profile_form}
        return render(request,'blogs/regview.html',context)

def signout(request):
    logout(request)
    return redirect('blogs:blogview')

class PostCreate(CreateView):
    model = Post
    fields = ('title','date','body','image','slug','category')

class PostUpdate(UpdateView):
    model = Post
    fields = ('title','date','body','image','slug','category')
    template_name_suffix = '_update_form'

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:blogview')

    def get(self, request, *args, **kwargs):
        """This is used because without it the get request needs a confirm delete template"""
        return self.post(request,*args, **kwargs)