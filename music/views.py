from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

#from music.forms import musicform
from django.views.generic.edit import CreateView

from music.models import Album, Song
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import UserForm
from django.views.generic import View


# def musicview(request):
#     albums = Album.objects.all()
#     return render(request,'music/musicview.html',{'albums':albums})
#
# def detail(request,album_id):
#     album = get_object_or_404(Album,pk = album_id)
#     return render(request,'music/detail.html',{'album':album})
#
# def favourite(request,album_id):
#     album = get_object_or_404(Album,pk=album_id)
#
#     var = request.POST.getlist('song')
#     for song_id in var:
#         fav_song = album.song_set.get(pk = song_id)
#         fav_song.is_favourite = True
#         fav_song.save()
#
#     return render(request,'music/detail.html',{'album':album})
#
#
class MusicView(generic.ListView):
    template_name = "music/musicview.html"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','title','genre','logo']

class SongCreate(CreateView):
    model = Song
    fields = ['album','file_type','song_title','is_favourite']

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('musicview')
        return render(request,self.template_name,{'form':form})