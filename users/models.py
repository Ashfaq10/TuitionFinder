from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    USER_TYPE =(
        ('student', 'Student'),
        ('tutor', 'Tutor')
    )
    user_type = models.CharField(max_length=100, choices=USER_TYPE)


