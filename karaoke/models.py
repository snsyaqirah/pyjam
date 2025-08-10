from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    lyrics_text = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.artist}"

    def lyrics(self):
        # Boleh parse ke JSON kalau nak
        return self.lyrics_text
