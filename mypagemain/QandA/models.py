from django.db import models
from django import forms 

# def min_length_3_validator(value):
# 	if len(value) < 3:
# 		raise forms.ValidationError('3글자 이상 입력해주세요')

class Userqa(models.Model):
    username = models.CharField(max_length=100, null = True)
    title = models.CharField(max_length=100, null = True)
    question = models.CharField(max_length=100, null = True)
    pub_date = models.DateField('date published', null = True)
    objects = models.Manager() 


    def __str__(self):
        return self.title

    # def summary(self):
    #     return self.question[:20]