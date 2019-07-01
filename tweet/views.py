import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q, QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from taggit.models import Tag

from tweet.forms import UserForm, UserProfileForm, TweetForm
from tweet.models import Tweet, UserProfile, Friend, Retweet


def homeview(request):


    if request.method == 'POST':
        tweet_form = TweetForm(request.POST,request.FILES)
        if tweet_form.is_valid():
            t = tweet_form.save(commit=False)
            t.user = request.user
            t.save()
            hashtagArray = re.findall(r'#(\w+)',t.tweet)
            for ht in hashtagArray:
                t.tags.add(ht)
            t.save()
        elif 'retweet' in request.POST:
            id = request.POST['retweet']
            rt = Tweet.objects.get(id=id)
            retweet = Retweet(user = request.user, owner = rt.user, tweet=rt.tweet, image=rt.image, tags = rt.tags, date=rt.date )
            retweet.save()
    else:
        tweet_form = TweetForm()
    tweets = Tweet.objects.filter(user=request.user)
    tags = Tag.objects.all()
    friend,created = Friend.objects.get_or_create(owner=request.user)
    users = friend.users.all()
    friends_tweets = []
    for fr in users:
        tweets = tweets | Tweet.objects.filter(user=fr)

    profile = UserProfile.objects.get(user=request.user)
    users = User.objects.exclude(username = request.user)
    retweets = Retweet.objects.filter(user=request.user)
    return render(request,'tweet/homeview.html',{'username':request.user,'tweets':tweets,'retweets':retweets,'form':tweet_form,'tags':tags, 'profile':profile,'users':users})

def user_login(request):
    if request.method =='POST':
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('tweet:homeview')
            else:
                return HttpResponse('Account Inactive')
        else:
            print("Failed login using username : {} and password : {}".format(username,password))
            return HttpResponse('Invalid details')
    else:
        return render(request,'tweet/login.html')


def signout(request):
    logout(request)
    return render(request,'tweet/homeview.html')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return render(request,'tweet/homeview.html')
        else:
            return HttpResponse("Error")

    elif request.method == 'GET':
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request, 'tweet/register.html',{'user_form':user_form,'profile_form':profile_form})

def userview(request,user):
    tweets = Tweet.objects.all()
    array =[]
    if request.method == 'POST':
        if 'btn-friend' in request.POST:
            friend, created= Friend.objects.get_or_create(owner = request.user)
            new_friend = User.objects.get(username= user)

            friend.users.add(new_friend)
            friend.save()
    for tweet in tweets:
        print(tweet.user.username)
        if(tweet.user.username == user):
            array.append(tweet)
    return render(request,'tweet/userview.html',{'array':array.reverse(),'user':user})

def tagview(request,tag):
    answer = '#'+tag
    tweets = Tweet.objects.filter(Q(tweet__contains=answer)) #query within filter statement
    print(answer)

    return render(request,'tweet/tagview.html',{'tweets':tweets})

def profileview(request):
    display_profile = UserProfile.objects.get(user=request.user)

    return render(request,'tweet/profileview.html',{'display_profile':display_profile})
