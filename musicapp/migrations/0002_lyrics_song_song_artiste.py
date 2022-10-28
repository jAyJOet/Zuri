# Generated by Django 4.1.2 on 2022-10-28 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyrics',
            name='Song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='Artiste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='musicapp.artiste'),
            preserve_default=False,
        ),
    ]
