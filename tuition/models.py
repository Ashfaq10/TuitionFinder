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
