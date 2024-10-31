from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    name = models.CharField(max_length=100)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    job_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    about = models.TextField()
    skills = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    reputation = models.IntegerField(default=0)
    answers_posted = models.PositiveIntegerField(default=0)
    questions_posted = models.PositiveIntegerField(default=0)
