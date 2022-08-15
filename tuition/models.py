from django.db import models

from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class Level(models.Model):
    current_class = models.CharField(max_length=100)
class Subject(models.Model):
    subject = models.CharField(max_length=100)

class Tuition(models.Model):
    provider = models.ForeignKey(USER_MODEL, on_delete= models.CASCADE, related_name='tuition_provided')
    tutor = models.ForeignKey(USER_MODEL, on_delete= models.CASCADE, related_name="tution_tutored", null= True)
    location = models.CharField(max_length=100)
    level = models.ManyToManyField(Level)
    subject = models.ManyToManyField(Subject)
    requirements = models.TextField()
    salary = models.CharField(max_length=50)


class Rating(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    student_rating_value = models.IntegerField(
        choices = RATING_CHOICES
    )
    tutor_rating_value = models.IntegerField(
        choices = RATING_CHOICES
    )
    review = models.TextField()

    tuition = models.ForeignKey(Tuition , on_delete= models.CASCADE)




# Create your models here.
