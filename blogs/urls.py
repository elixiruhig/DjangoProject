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
from blogs import views

app_name = 'blogs'

urlpatterns = [

    path('',views.blogview,name='blogview'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$', views.signout, name='signout'),
    url(r'^(?P<slug>[-\w]+)/$',views.postdetail,name = 'postdetail'),
    url(r'^post/add$',views.PostCreate.as_view(),name = 'post-create'),
    url(r'^post/(?P<pk>[0-9]+)$',views.PostUpdate.as_view(),name = 'post-update'),
    url(r'^post/(?P<pk>[0-9]+)/delete$',views.PostDelete.as_view(),name = 'post-delete')
]
