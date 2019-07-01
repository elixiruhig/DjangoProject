"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from music import views

urlpatterns = [
    path('',views.MusicView.as_view(),name='musicview'),

    url(r'^register/$',views.UserFormView.as_view(),name = 'UserForm'),

    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name = 'detail'),

    url(r'album/add/$',views.AlbumCreate.as_view(),name = 'album-create'),
     #url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name = 'favourite'),
    url(r'song/add/$', views.SongCreate.as_view(), name='song-create')

]
