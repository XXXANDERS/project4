from django.db import models


class Image(models.Model):
    TYPE_CHOICES = (
        (0, 'anime'),
        (1, 'manga'),
        (2, 'author'),
        # (3, 'user'),
    )
    entity_id = models.IntegerField()
    src = models.ImageField(upload_to='images/%Y/%m/%d/')
    entity_type = models.IntegerField(choices=TYPE_CHOICES)
