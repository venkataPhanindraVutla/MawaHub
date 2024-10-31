from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")
def register(request):
    return render(request,'register.html')

def sidebar(request):
    return render(request,'sidebar.html')


def add_question(request):
    return render(request,'add_question.html')

def all_questions(request):
    resp = questions.objects.all()
    dic =[
        {
            "title": "How to build a StackOverflow clone?",
            "question": "I want to build a StackOverflow clone. Where can I get some help?",
            "author": "Santhi",
            "date": "1m ago",
            "score": 1,
        },
        {
            "title": "How to import pandas?",
            "question": "Please help me import pandas. Where can I get some help?",
            "author": "Santhi",
            "date": "1m ago",
            "score": 1,
        }
        ]
    return render(request,'all_questions.html',{'questions':dic,"resp":resp})

def update_profile(request):
    if request.method == 'POST':
        # Fetch and update profile details
        request.user.profile.username = request.POST['username']
        request.user.profile.email = request.POST['email']
        request.user.profile.about = request.POST['about']
        request.user.profile.skills = request.POST['skills']
        request.user.profile.address = request.POST['address']
        request.user.profile.phone = request.POST['phone']
        request.user.profile.reputation = request.POST['reputation']
        request.user.profile.save()
        return redirect('user_profile')
    return render(request, 'edit_profile.html')