from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'karaoke/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'karaoke/song_detail.html', {"song": song})

def song_lyrics_json(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return JsonResponse(song.lyrics(), safe=False)
