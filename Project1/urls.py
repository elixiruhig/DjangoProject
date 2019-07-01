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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('myapp/',include('myapp.urls')),
    path('blogs/',include('blogs.urls')),
    path('music/',include('music.urls')),
    path('todolist/',include('todolist.urls')),
    path('quotes/',include('quotes.urls')),
    path('tts/',include('tts.urls')),
    path('translate/',include('translate.urls')),
    path('visualization/',include('visualization.urls')),
    path('s2t/',include('s2t.urls')),
    path('quiz/',include('quiz.urls')),
    path('tweet/',include('tweet.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)