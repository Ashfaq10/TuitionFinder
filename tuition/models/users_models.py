from contextlib import nullcontext
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    USER_TYPE =(
        ('student', 'Student'),
        ('tutor', 'Tutor')
    )
    user_type = models.CharField(max_length=100, choices=USER_TYPE)
    phone = models.CharField(max_length=15, null= True)
    location = models.CharField(max_length=100, null= True)
    about = models.TextField(null=True)
    photo = models.ImageField(upload_to='media/images/profile_pictures/', null=True, blank=True)
    
    @property
    def rating(self):
        return 5


