# forms.py

from django import forms 
from .models import Userqa, Answerqa

class UserqaForm(forms.ModelForm): 
    class Meta:
        model = Userqa
        fields = ('title', 'question', 'author', 'reader')
        labels = {  # input의 label 정의
            'title' : '질문 제목' ,
            'question' : '내용',
            'author' : '작성자',
            'reader' : '받는사람',
        }
        widgets = { # form의 특징과 속성 정의
            'title' : forms.TextInput ( attrs = {'class' : 'title'}),
            'question' : forms.TextInput ( attrs = {'class' : 'question', 'cols': 60, 'rows': 10}),
            'reader' : forms.TextInput ( attrs = {'class' : 'title'}),
        }

class UserqaForm2(forms.ModelForm): 
    class Meta:
        model = Answerqa
        fields = ('a_title', 'answer')
        labels = {  # input의 label 정의
            'a_title' : '답변 제목' ,
            'answer' : '내용',
        }
        widgets = { # form의 특징과 속성 정의
            'a_title' : forms.TextInput ( attrs = {'class' : 'title'}),
            'answer' : forms.TextInput ( attrs = {'class' : 'question', 'cols': 60, 'rows': 10}),
        }

