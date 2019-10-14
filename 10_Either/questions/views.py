from django.shortcuts import render, redirect
from .models import Question, Choice, Answer
import random
# Create your views here.

def index(request):
    questions = Question.objects.all()

    random_question = random.choice(questions)

    context = {
        'questions':questions,
        'random_question':random_question,
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        question = Question.objects.create(pick_1=request.POST.get('pick_1'), pick_2=request.POST.get('pick_2'))
        choice = Choice.objects.create(pick_1_count=0, pick_2_count=0, question=question)

        return redirect('questions:index')
    else:
        return render(request, 'create.html')

def detail(request, id):
    question = Question.objects.get(id=id)
    # choice = question.choice_set
    context = {
        'question':question,
        # 'choice':choice,
    }
    return render(request, 'detail.html',context)

def update(request, id):
    question = Question.objects.get(id=id)

    if request.method == 'POST':
        question.pick_1 = request.POST.get('pick_1')
        question.pick_2 = request.POST.get('pick_2')
        question.save()

        return redirect('questions:detail', question.id)

    else:
        context = {
            'question':question
        }
        
        return render(request, 'update.html', context)

def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()

    return redirect('questions:index')

def count(request, choice_id, select):
    choice = Choice.objects.get(id=choice_id)
    if select == 1:
        choice.pick_1_count += 1
    else:
        choice.pick_2_count += 1

    choice.save()    

    return redirect('questions:detail', choice.question.id)

def answer_create(request, question_id):
    Answer.objects.create(answer=request.POST.get('answer'), question=Question.objects.get(id=question_id))

    return redirect('questions:detail', question_id)

def answer_delete(request, question_id, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.delete()

    return redirect('questions:detail', question_id)