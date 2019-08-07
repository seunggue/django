from django.shortcuts import render

# Create your views here.
def ping(request):

    return render(request, 'ping.html')

def pong(request):
    user_name = request.GET.get('name')
    user_age = request.GET.get('age')
    context = {
        'user_name': user_name,
        'user_age': user_age,
    }
    
    return render(request, 'pong.html', context)

def post_ping(request):
    return render(request, 'post_ping.html')

def post_pong(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    context = {
        'username': username,
        'password': password,
    }
    return render(request, 'post_pong.html', context)

def static_example(request):
    return render(request, 'static_example.html')