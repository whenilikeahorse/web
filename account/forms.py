from django import forms
from django.contrib.auth.models import User
from .models import User,Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'usernameform'}),
        }

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False

    class Meta():
        model = Profile
        fields = ('file','age','gender', 'occupation','company','major','interest')
        widgets = {
            # 'file': forms.FileInput(attrs={'class': 'fileform'}),
            'age': forms.TextInput(attrs={'class': 'ageform'}),
            'gender': forms.Select(attrs={'class': 'genderform'}),
            'occupation' : forms.TextInput(attrs={'class': 'occupationform'}),
            'company' : forms.TextInput(attrs={'class': 'companyform'}),
            'major' : forms.TextInput(attrs={'class': 'majorform'}),
            'interest' : forms.TextInput(attrs={'class': 'interestform'}),
        }