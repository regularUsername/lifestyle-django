# um type hint Video zu nutzen vor Videos deklaration
from __future__ import annotations

from django.db import models
from django.utils.text import slugify


# Create your models here.


def validate_embedcode(value):
    pass


def video_thumbnail_path(instance: Video, filename: str):
    return f"video_thumbnails/{slugify(instance.title)}.{filename.split('.')[-1]}"


class Video(models.Model):

    class Meta:
        ordering = ['-pub_date']

    title = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=200, blank=True)

    thumbnail = models.ImageField(upload_to=video_thumbnail_path)
    embedcode = models.TextField(validators=[validate_embedcode])

    pub_date = models.DateTimeField('date published', auto_now=True)
    duration = models.DurationField()
    def __str__(self):
        return self.title
