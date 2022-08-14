from django.db import models

from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class Level(models.Model):
    current_class = models.CharField(max_length=100)
class Subject(models.Model):
    subject = models.CharField(max_length=100)

class Tuition(models.Model):
    name = models.ForeignKey(USER_MODEL, on_delete= models.CASCADE)
    location = models.CharField(max_length=100)
    level = models.ManyToManyField(Level)
    subject = models.ManyToManyField(Subject)
    requirements = models.TextField()
    salary = models.CharField(max_length=50)

    

# class Rating(models.Model):
#     RATING_CHOICES = (
#         ('1', '1 star'),
#         ('2', '2 stars'),
#         ('3', '3 stars'),
#         ('4', '4 stars'),
#         ('5', '5 stars'),
#     )
#     rating_value = models.IntegerField(
#         choices = RATING_CHOICES
#     )
#     user = models.ForeignKey(USER_MODEL, on_delete= models.CASCADE)


# Create your models here.
