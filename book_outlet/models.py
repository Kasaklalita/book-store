from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 50)
    rating = models.IntField()
    #the id field is created automatically
