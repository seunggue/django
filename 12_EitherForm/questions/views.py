from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'questions/index.html')

def create(request):
    if request.method == "POST":
        pass

    else:

        return render(request, 'questions/form.html')