from django.db import models
from tinymce.models import HTMLField

from django.conf import settings


class Kategorie(models.Model):
    name = models.CharField(max_length=30)
    beschreibung = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Kategorien'

    def __str__(self):
        return self.name


class Rezept(models.Model):
    class Meta:
        verbose_name_plural = 'Rezepte'
    title = models.CharField(max_length=200)
    # TODO das hier vernünftig einrichten
    thumbnail = models.ImageField(upload_to='uploads/', blank=True)
    # text = models.TextField()

    # tinymce richtext
    content = HTMLField()

    kategorien = models.ManyToManyField(Kategorie, blank=True)

    pub_date = models.DateTimeField('date published')

    # favorited_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'rezept'], name='unique_favorite')
        ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name="User")
    rezept = models.ForeignKey(Rezept, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.get_username()} loves {self.rezept.title}"
