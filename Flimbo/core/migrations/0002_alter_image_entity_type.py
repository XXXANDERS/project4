# Generated by Django 3.2.9 on 2021-11-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='entity_type',
            field=models.IntegerField(choices=[(0, 'anime'), (1, 'manga'), (2, 'author')]),
        ),
    ]
