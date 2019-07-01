from django.db import models
# Create your models here.
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length =250, blank=False, null=False)
    title = models.CharField(max_length = 100, blank=False, null=False)
    genre = models.CharField(max_length = 50, blank=False, null=False)
    logo = models.CharField(max_length=500)

    def __str__(self):
        return self.title + ' - ' + self.artist

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 20)
    song_title = models.CharField(max_length = 250, blank=False, null=False)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.album.pk})