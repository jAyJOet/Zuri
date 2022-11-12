from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artiste, Song
from .serializers import artisteSerializers, songSerializers

def index(request):
    pass
@api_view(['GET', 'POST'])
def Artiste_list(request,format=None):
    if request.method == 'GET':
        artistes = Artiste.objects.all()
        serializer = artisteSerializers(artistes, many=True )
        return JsonResponse({"Artistes":serializer.data})
    if request.method == 'POST':
        serializer = artisteSerializers(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def Song_list(request,format=None):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = songSerializers(songs, many=True )
        return JsonResponse({"Songs":serializer.data})
        if request.method == 'POST':
            serializer = songSerializers(data=request.data)
            if serializer.is_valid:
                serializer.save()
                return Response(serializer.data, status =status.HTTP_201_CREATED)
@api_view(['GET', 'PUT','DELETE'])
def Artiste_detail (request,id, format=None):
    try:
        artiste=Artiste.objects.get(pk=id)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = artisteSerializers(artiste)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = artisteSerializers(artiste,data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT','DELETE'])
def Song_detail (request,id, format=None):
    try:
        song=Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = songSerializers(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = songSerializers(song,data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)