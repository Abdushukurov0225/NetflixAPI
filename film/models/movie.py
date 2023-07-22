from django.db import models


class Movie(models.Model):
    actor = models.ManyToManyField('film.Actor')
    name = models.CharField(max_length=100, blank=False, null=False)
    imdb = models.FloatField(blank=True)
    genre = models.CharField(max_length=20)
    year = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
