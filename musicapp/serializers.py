from rest_framework import serializers
from .models import Artiste,Song, Lyrics
class artisteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id','first_name', 'last_name','age']
class songSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','Artiste', 'title','date_released','likes','Artiste_id']
        