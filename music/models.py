# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse



# Create your models here. Red pk 1
class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):  # a string representation of this object.
        return self.album_title + ' ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # can use on_update=models.WHATEVER.
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=255)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
