from django.shortcuts import render
from .models import Student
# Create your views here.

def user(request):
    
    return render(request,'user.html',{"data":data})