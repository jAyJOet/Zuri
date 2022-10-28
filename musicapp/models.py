from ast import Import

from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.
class Artiste (models.Model):
   first_name = models.CharField(max_length=50)
   last_name  = models.CharField(max_length=50)
  # stage_name  = models.CharField(max_length=50)
   age        = models.IntegerField()
   





   def __str__(self) :
          return self.first_name
class Song (models.Model):
   Artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT)
   title = models.CharField(max_length=50)
   date_released  =models.DateField(default=datetime.today)
   likes       = models.IntegerField()
   artiste_id      = models.IntegerField()


   def __str__(self) :
          return self.title
   
class Lyrics (models.Model):
   Song = models.OneToOneField(Song, on_delete=models.CASCADE)
   content = models.CharField(max_length=5000)
   song_id = models.IntegerField()
   