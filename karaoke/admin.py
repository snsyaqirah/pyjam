from django.contrib import admin
from django.utils.html import format_html
from .models import Song, SongRequest

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'duration_seconds', 'audio_preview', 'created_at']
    list_filter = ['artist', 'created_at']
    search_fields = ['title', 'artist']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'artist', 'audio_file', 'duration_seconds')
        }),
        ('Lyrics Timing', {
            'fields': ('lyrics_json',),
            'description': 'Enter timed lyrics as JSON array. Example: [{"time": 0, "text": "First line"}, {"time": 5, "text": "Second line"}]'
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def audio_preview(self, obj):
        if obj.audio_file:
            return format_html(
                '<audio controls style="width: 200px;"><source src="{}" type="audio/mpeg"></audio>',
                obj.audio_file.url
            )
        return "No audio"
    audio_preview.short_description = "Audio Preview"

@admin.register(SongRequest)
class SongRequestAdmin(admin.ModelAdmin):
    list_display = ['song', 'requester_name', 'requester_email', 'is_processed', 'requested_at']
    list_filter = ['is_processed', 'requested_at', 'song']
    search_fields = ['requester_name', 'requester_email', 'song__title']
    readonly_fields = ['requested_at']
    
    actions = ['mark_as_processed']
    
    def mark_as_processed(self, request, queryset):
        queryset.update(is_processed=True)
    mark_as_processed.short_description = "Mark selected requests as processed"