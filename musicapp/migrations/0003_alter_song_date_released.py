# Generated by Django 4.1.2 on 2022-10-28 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_lyrics_song_song_artiste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]