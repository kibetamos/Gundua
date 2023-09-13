# forms.py
from django import forms
from .models import Crime

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['date', 'time', 'location', 'occur', 'action', 'type']


    # Additional fields can be added here, if needed
    # attachments = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
