from django import forms
from .models import SongRequest

class SongRequestForm(forms.ModelForm):
    class Meta:
        model = SongRequest
        fields = ['requester_name', 'requester_email', 'message']
        widgets = {
            'requester_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'requester_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional message or special requests',
                'rows': 3
            }),
        }