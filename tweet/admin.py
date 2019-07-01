from django.contrib import admin

# Register your models here.
from tweet.models import Tweet, UserProfile, Friend, Retweet

admin.site.register(Tweet)
admin.site.register(UserProfile)
admin.site.register(Friend)
admin.site.register(Retweet)