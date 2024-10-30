from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "base.html")

def login(request):
    return render(request, "login.html")
def register(request):
    return render(request,'register.html')

def all_questions(request):
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
    return render(request,'all_questions.html',{'questions':dic})