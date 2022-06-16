from pyexpat import model
from statistics import mode
from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=100)


class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_descriptions = models.TextField()
    banner=models.CharField(max_length=100)
    main=models.BooleanField(default=False)