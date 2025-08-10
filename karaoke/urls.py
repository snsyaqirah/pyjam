from django.urls import path
from . import views

app_name = "karaoke"

urlpatterns = [
    path("songs/", views.song_list, name="song_list"),
    path("song/<int:pk>/", views.song_detail, name="song_detail"),
    path("song/<int:pk>/lyrics.json", views.song_lyrics_json, name="song_lyrics_json"),
    path("song/<int:pk>/karaoke/", views.karaoke_player, name="karaoke_player"),
    path("song/<int:pk>/request/", views.song_request, name="song_request"),
]