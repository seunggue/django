from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):

    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')

    todo = Todo.objects.create(title=title, content=content, due_date=due_date)

    return redirect('/todos/')

