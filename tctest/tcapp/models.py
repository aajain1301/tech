from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    color = models.CharField(max_length=30)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def get_absolute_url(self):
         return reverse("tcapp:detailview",kwargs={'pk':self.pk})
