from django.test import TestCase

# Create your tests here.
from .models import Album,Song

class AlbumModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Album.objects.create(artist='abc', title='xyz', genre='pop', logo='http://google.com')

    def test_artist_name(self):
        album = Album.objects.get(id=2)
        field_label = album._meta.get_field('artist').verbose_name
        self.assertEquals(field_label, 'artist')

    def test_title(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_genre(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_logo(self):
        album = Album.objects.get(id=1)
        field_label = album._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'logo')

    def test_str_method(self):
        album = Album.objects.get(id=1)
        expected_name = album.title + " - " + album.artist
        self.assertEquals(expected_name, str(album))

    def test_absolute_url(self):
        album= Album.objects.get(id=1)
        self.assertEquals(album.get_absolute_url(),'/music/1/')

