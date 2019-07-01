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

from tweet import views
app_name = 'tweet'
urlpatterns = [
    path('',views.homeview,name='homeview'),
    url(r'^login$',views.user_login, name = 'login'),
    url(r'^register$',views.register, name = 'register'),
    url(r'^signout$',views.signout, name = 'signout'),
    url(r'^(?P<user>[\w]+)/$',views.userview, name = 'userview'),
    url(r'^tag=(?P<tag>[\w]+)/$', views.tagview, name='tagview'),
    url(r'^profile$',views.profileview, name = 'profile')

]
