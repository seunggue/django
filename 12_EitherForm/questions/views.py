from django.shortcuts import render
from .forms import QuestionForm

# Create your views here.
def index(request):
    return render(request, 'questions/index.html')

def create(request):
    if request.method == "POST":
        pass

    else:
        form = QuestionForm()
        context = {
            'form':form,
        }

        return render(request, 'questions/form.html', context)
        # return render(request, 'questions/form.html', {'form':form})