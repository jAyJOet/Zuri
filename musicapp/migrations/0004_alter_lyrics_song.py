# Generated by Django 4.1.2 on 2022-11-05 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_song_date_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='Song',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
    ]
