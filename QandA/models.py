from django.db import models
from django import forms 
from django.contrib.auth.models import User
from django.contrib import auth

class Userqa(models.Model):
    author = models.CharField(max_length=100, null = True)
    title = models.CharField(max_length=100, null = True)
    question = models.CharField(max_length=100, null = True)
    pub_date = models.DateField('date published', null = True)
    reader = models.CharField(max_length=100, null = True)
    a_title = models.CharField(max_length=100, null = True)
    answer = models.CharField(max_length=100, null = True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    