from django.db import models
from django import forms 
# Create your models here.

class selfqa(models.Model):
    username = models.CharField(max_length=100, null = True)
    question = models.CharField(max_length=500, null = True)
    answer = models.CharField(max_length=500, null = True)
    pub_date = models.DateField('date published', null = True)
    objects = models.Manager() 

    def __str__(self):
        return self.title