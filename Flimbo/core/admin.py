from django.contrib import admin
from django.contrib.admin import ModelAdmin

from core.models import Image


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    pass
