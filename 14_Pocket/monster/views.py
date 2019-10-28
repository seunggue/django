from django.shortcuts import render, redirect, get_object_or_404
from .models import Monster, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

# Create your views here.
def index(request):
    monsters = Monster.objects.all()
    context = {
        'monsters': monsters, 
    }
    return render(request, 'monster/index.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            
            content_title = request.POST.get('content_title')
            choice = request.POST.get('choice')
            monster_name = request.POST.get('monster_name')
            monster_image = request.FILES.get('monster_image')
            monster_detail = request.POST.get('monster_detail')
            monster_size = request.POST.get('monster_size')
            user = request.user
            monster = Monster.objects.create(content_title=content_title,choice=choice, monster_name=monster_name, monster_image=monster_image, monster_detail=monster_detail, monster_size=monster_size, user=user)
            return redirect('monster:index')
        else:
            return render(request, 'monster/form.html')
    else:  
        return render(request, 'monster/warning.html')


def detail(request, id):
    monster = Monster.objects.get(id=id)
    comment_form = CommentForm()
    like_count = monster.like_users.count()
    context = {
        'monster':monster,
        'comment_form' : comment_form,
        'like_count':like_count
    }
    return render(request, 'monster/detail.html', context)

@login_required
def delete(request, id):
    monster = Monster.objects.get(id=id)
    monster.delete()
    return redirect('monster:index')

@login_required
def update(request, id):
    monster = Monster.objects.get(id=id)
    if request.method == 'POST':
        choice = request.POST.get('choice')
        content_name = request.POST.get('content_name')
        content_image = request.FILES.get('content_image')
        content_detail = request.POST.get('content_detail')
        content_size = request.POST.get('content_size')
        user = request.user

        monster.choice = choice
        monster.content_name = content_name
        monster.content_image = content_image
        monster.content_detail = content_detail
        monster.content_size = content_size
        
        monster.save()
        return redirect('monster:detail' ,id)

    else:

        return render(request, 'monster/update.html', {'monster':monster})

@login_required
def comment_create(request, id):
    monster = Monster.objects.get(id=id)

    if request.method =='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.monster = monster
            comment.user = request.user
            comment.save()
            return redirect('monster:detail' ,id)

@login_required
def comment_delete(request, monster_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('monster:detail', monster_id)

def like(request, id):
    monster = get_object_or_404(Monster, id=id)
    user = request.user
    if user in monster.like_users.all():
        monster.like_users.remove(user)
    else:
        monster.like_users.add(user)

    return redirect('monster:detail', id)
        


