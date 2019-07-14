# forms.py

from django import forms 
from .models import Userqa

class UserqaForm(forms.ModelForm): 
    class Meta:
        model = Userqa
        fields = ('title', 'question')
        labels = {  # input의 label 정의
            'title' : '질문 제목' ,
            'question' : '내용',
        }
        widgets = { # form의 특징과 속성 정의
            'title' : forms.TextInput ( attrs = {'class' : 'title'}),
            'question' : forms.TextInput ( attrs = {'class' : 'question', 'cols': 60, 'rows': 10}),
        }

