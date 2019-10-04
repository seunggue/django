from django.shortcuts import render, redirect
from .models import Cre

# Create your views here.
def start(request):
    return render(request, 'start.html')

def end(request):
    user_name = request.GET.get('name')
    user_age = request.GET.get('age')
    context = {
        'user_name': user_name,
        'user_age': user_age,
    }
    return render(request, 'end.html', context)

def create(request):
    user_name = request.GET.get('name')
    user_age = request.GET.get('age')

    cre = Cre(name=user_name, age=user_name)
    cre.save()
    return render(request, 'create.html')

def index(request):
    cres = Cre.objects.all()
    context = {
        'cres':cres,
    }
    return render(request, 'index.html', context)