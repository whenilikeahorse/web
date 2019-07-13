from django.db import models
from django import forms 

# def min_length_3_validator(value):
# 	if len(value) < 3:
# 		raise forms.ValidationError('3글자 이상 입력해주세요')

class Userqa(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100, verbose_name = "질문 제목", null = True)
    question = models.CharField(max_length=100, verbose_name = "내용")

    def __str__(self):
        return self.title