from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext as _
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(default=datetime.now())
    body = models.TextField()
    image = models.URLField(blank=True)
    slug = models.SlugField(_('slug'),max_length=60,blank=True)
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('blogs:blogview')

class UserProfileInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.user.username
