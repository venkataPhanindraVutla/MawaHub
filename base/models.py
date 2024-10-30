from django.db import models

# Create your models here.
class questions(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField()
    score = models.IntegerField()