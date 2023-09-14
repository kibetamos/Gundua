# forms.py
from django import forms
from .models import Crime

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['id_no', 'first_name','last_name', 'date', 'time', 'location', 'occur', 'action', 'type']

        widgets = {
                    'date': forms.DateInput(attrs={'type': 'date'}),
                    'time': forms.TimeInput(attrs={'type': 'time'}),
                }
    # Additional fields can be added here, if needed
    # attachments = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
