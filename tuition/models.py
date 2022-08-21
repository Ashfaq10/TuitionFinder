from django.db import models

from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

# class Level(models.Model):
#     class_name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.class_name
# class Subject(models.Model):
#     subject = models.CharField(max_length=100)

class Tuition(models.Model):
    provider = models.ForeignKey(USER_MODEL, on_delete= models.CASCADE, related_name='tuition_provided')
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null= True)
    level = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    requirements = models.TextField()
    salary = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)





# Create your models here.
