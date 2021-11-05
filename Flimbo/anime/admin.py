from django.contrib import admin
from django.contrib.admin import ModelAdmin

from anime.models import Anime, Manga, Author


@admin.register(Anime)
class AnimeAdmin(ModelAdmin):
    pass


@admin.register(Manga)
class MangaAdmin(ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    pass
