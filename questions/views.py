from django.shortcuts import render
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