from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField()
    score = models.IntegerField()
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField()
    score = models.IntegerField()
    