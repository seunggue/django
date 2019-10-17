from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            return redirect('todos:index')
    else:
        form = UserCreationForm()
    
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('todos:index')

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')

    else:
        form = AuthenticationForm()

    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html', context)