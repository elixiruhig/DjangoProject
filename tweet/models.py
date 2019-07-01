from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from taggit.managers import TaggableManager


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tweet = models.CharField(max_length=140, blank=False, null=False)
    date = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='user_images',blank=True,null=True)
    tags = TaggableManager()


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name= models.CharField(max_length=100, blank=False, null=False)
    profile_pic = models.ImageField(upload_to='profile_pic', default='profile_pic/default')

    def __str__(self):
        return self.user.username

class Friend(models.Model):
    users = models.ManyToManyField(User)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner',null=True)

class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='author')
    tweet = models.CharField(max_length=140, blank=False, null=False)
    date = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='user_images',blank=True,null=True)
    tags = TaggableManager()
