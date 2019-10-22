from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')

    else:
        forms = PostForm()
    context = {
        'forms':forms
    }
    return render(request, 'posts/form.html', context)