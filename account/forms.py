from django import forms
from django.contrib.auth.models import User
from .models import User,Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False

    class Meta():
        model = Profile
        fields = ('file','age', 'occupation')