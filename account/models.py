from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from imagekit.models import ImageSpecField #image
from imagekit.processors import ResizeToFill #image



# Create your models here.
class Profile(models.Model):
     GENDER_MALE = 'm'
     GENDER_FEMALE = 'f'
     GENDER_CHOICES = (
        (GENDER_MALE, '남성'),
        (GENDER_FEMALE, '여성'),
     )
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     gender = models.TextField(max_length=10,blank=True,choices=GENDER_CHOICES)
     age = models.TextField(max_length=10,blank=True)
     occupation = models.TextField(max_length=20,blank=True)
     major = models.TextField(max_length=10,blank=True)
     company = models.TextField(max_length=10,blank=True)
     interest = models.TextField(max_length=10,blank=True)
     file = models.FileField(null=True)

     def __str__(self):
          return self.user.username

# Profile Model 에서 발생하는 signals를 정의
# signals는 User instance를 생성/ 수정 할 때 자동으로 created/updated함

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()