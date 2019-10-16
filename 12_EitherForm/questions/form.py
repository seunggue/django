from django import forms
from .models import Questions

class QuestionForm(forms.modelForm):
    class Meta:
        model = Questions
        fields = '__all__'