from django.db import models


class Anime(models.Model):
    entity_type = 'anime'

    title = models.CharField(max_length=255)
    description = models.TextField(4095)
    release_date = models.DateField()


class Manga(models.Model):
    entity_type = 'manga'

    title = models.CharField(max_length=255)
    description = models.TextField(4095)
    release_date = models.DateField()


class Author(models.Model):
    entity_type = 'author'

    nickname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField(max_length=4095)
    animes = models.ManyToManyField('Anime', related_name='authors')
    birth_date = models.DateField()

# ANIME: photo, title, description, authors, release_date,
# AUTHOR: photo, nick, first_name, last_name, description, animes, birth_date,
