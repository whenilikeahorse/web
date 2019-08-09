from django.db import models
from django.contrib.auth.models import User
from .choice import * 

class portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=20)
    content_type = models.IntegerField(default=1 ,choices=TYPE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager() 

    def __str__(self):
        return self.title