from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from blogs.api import views

urlpatterns = [

    url(r'^$',views.PostListAPIView.as_view(),name='postlistview'),
    url(r'^create/$',views.PostCreateAPIView.as_view(),name='createview'),
    url(r'^(?P<slug>[-\w]+)/$',views.PostDetailAPIView.as_view(),name='detailview'),
    url(r'^(?P<slug>[-\w]+)/delete/$',views.PostDeleteAPIView.as_view(),name='deleteview'),
    url(r'^(?P<slug>[-\w]+)/update/$',views.PostUpdateAPIView.as_view(),name='updateview'),

]