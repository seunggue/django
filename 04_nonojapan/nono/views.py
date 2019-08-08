from django.shortcuts import render
from .models import Nono

# Create your views here.
def index(request):
    nonos = Nono.objects.all()
    context = {
        'nonos': nonos,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    product = request.GET.get('product')
    replace = request.GET.get('replace')
    img_url = request.GET.get('img_url')
    category = request.GET.get('category')

    nono = Nono(product=product, replace=replace, img_url=img_url, category=category)
    nono.save()

    return render(request, 'create.html')