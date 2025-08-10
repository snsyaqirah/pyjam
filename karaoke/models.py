from django.db import models
from django.core.validators import FileExtensionValidator
import json

class Song(models.Model):
    title = models.CharField(max_length=200, help_text="Song title")
    artist = models.CharField(max_length=200, help_text="Artist name")
    audio_file = models.FileField(
        upload_to='songs/audio/',
        validators=[FileExtensionValidator(['mp3', 'wav', 'ogg'])],
        help_text="Upload MP3, WAV, or OGG file"
    )
    lyrics_json = models.TextField(
        help_text='Timed lyrics in JSON format: [{"time": 0, "text": "First line"}, {"time": 5, "text": "Second line"}]',
        default='[]'
    )
    duration_seconds = models.IntegerField(
        default=180,
        help_text="Song duration in seconds (for admin timing control)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'artist']

    def __str__(self):
        return f"{self.title} - {self.artist}"

    def get_lyrics_list(self):
        """Parse JSON lyrics into Python list"""
        try:
            return json.loads(self.lyrics_json)
        except json.JSONDecodeError:
            return []

    def get_lyrics_text(self):
        """Get plain text lyrics for display"""
        lyrics_list = self.get_lyrics_list()
        return '\n'.join([item.get('text', '') for item in lyrics_list])


class SongRequest(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='requests')
    requester_name = models.CharField(max_length=100)
    requester_email = models.EmailField()
    message = models.TextField(blank=True, help_text="Optional message")
    requested_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-requested_at']

    def __str__(self):
        return f"{self.requester_name} requested {self.song.title}"