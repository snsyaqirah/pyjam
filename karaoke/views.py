from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Song, SongRequest
from .forms import SongRequestForm

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'karaoke/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'karaoke/song_detail.html', {"song": song})

def karaoke_player(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'karaoke/karaoke_player.html', {"song": song})

def song_lyrics_json(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return JsonResponse(song.get_lyrics_list(), safe=False)

def song_request(request, pk):
    song = get_object_or_404(Song, pk=pk)
    
    if request.method == 'POST':
        form = SongRequestForm(request.POST)
        if form.is_valid():
            song_request = form.save(commit=False)
            song_request.song = song
            song_request.save()
            
            # Send email notification (in development, prints to console)
            try:
                send_mail(
                    f'New Song Request: {song.title}',
                    f'User {song_request.requester_name} ({song_request.requester_email}) has requested the song "{song.title}" by {song.artist}.\n\nMessage: {song_request.message}',
                    'admin@pyjam.com',
                    ['admin@yourdomain.com'],  # Change this to your email
                    fail_silently=False,
                )
            except:
                pass  # Email sending failed, but request is still saved
            
            messages.success(request, f'Your request for "{song.title}" has been submitted!')
            return redirect('karaoke:song_list')
    else:
        form = SongRequestForm()
    
    return render(request, 'karaoke/song_request.html', {
        'song': song,
        'form': form
    })