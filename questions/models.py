from django.db import models
from django.utils import timezone
from users.models import Student

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-score', '-date']