from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from .forms import PostForm
from .models import HashTag, Post
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    real_users = User.objects.all()
    posts = Post.objects.all()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    context = {
        'real_users':real_users,
        'posts':posts,


    }

    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for word in post.content.split():
                if word.startswith('#'):
                    #hashtag추가
                    hashtag = HashTag.objects.get_or_create(content=word)[0] #(obj, True or False)
                    post.hashtags.add(hashtag)
            return redirect('posts:index')
    else:
        form = PostForm()
        context = {
            'form':form
        }
        return render(request, 'posts/form.html', context)

def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.Post, instance=post)
        if form.is_valid():
            post = form.save()
            post.hashtags.clear()

            for word in post.content.split():
                if word.startswith('#'):
                    #hashtag추가
                    hashtag = HashTag.objects.get_or_create(content=word)[0] #(obj, True or False)
                    post.hashtags.add(hashtag)
            return redirect('posts:index')


    else:
        form = PostForm(instance=post)
        context = {
            'form':form
        }
        return render(request, 'posts/form.html', context)

def hashtags(request, id):
    hashtag = get_object_or_404(HashTag, id=id)
    posts = hashtag.taged_post.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)

def like(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user
    if user in post.likes_users.all():
        post.likes_users.remove(user)
    else:
        post.likes_users.add(user)
    return redirect('posts:index')

# def comment_create(request, id):
#     comment_content = request.POST.get('comment_content')
#     comment_user = request.user
#     comment = Comment.objects.create

