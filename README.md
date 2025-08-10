# pyjam
# PyJam Karaoke 🎤

A simple Django karaoke app with timed lyrics.

## Features
- Upload songs with audio + timed lyrics.
- Lyrics displayed in sync with the song.
- Admin can edit timing via JSON.

## Requirements
- Python 3.10+
- Django 5.x
- A virtual environment (venv) recommended.

## Installation
```bash
# Clone repository
git clone <your_repo_url>
cd pyjam

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Migrate database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

# Usage
1. Visit http://127.0.0.1:8000/admin/ to log in.
2. Add new Song with:
    - Title
    - Artist
    - Audio file (MP3)
    - Lyrics JSON like:
        [
        {"time": 0, "text": "First line"},
        {"time": 5, "text": "Second line"}
        ]
3. Visit /songs/ to see the list.
4. Click a song to view karaoke player.