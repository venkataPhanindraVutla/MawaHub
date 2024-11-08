from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def questions(request):
    return render(request, "all_questions.html", {
        "questions": Question.objects.all()
    })

def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = question.answer_set.all()
    return render(request, "the_question_page.html", {
        "question": question,
        "answers": answers
    })
    
def add_question(request):
    if request.method == "GET":
        return render(request, "add_question.html")
    question_title = request.POST['question_title']
    question_text = request.POST['question']
    new = Question.objects.create(title=question_title, question=question_text, author=request.user)
    return redirect("question", question_id=new.id)
        