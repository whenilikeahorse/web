# forms.py

from django import forms 
from .models import Userqa

class UserqaForm(forms.ModelForm): 
    class Meta:
        model = Userqa
        fields = ('title', 'question')

