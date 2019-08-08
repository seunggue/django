from django.shortcuts import render, redirect
from.models import Question, Answer


# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    content = request.GET.get('content')

    question = Question()
    question.title = title
    question.user = user
    question.content = content
    question.save()

    return redirect('/questions/')

def index(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    context = {
        'questions':questions,
        'answers': answers,
    }
    return render(request, 'index.html', context)

def answer_create(request, question_id):
    content = request.GET.get('content')
    
    question = Question.objects.get(id=question_id)

    answer = Answer()
    answer.content = content
    answer.question = question
    answer.save()

    return redirect('/questions')