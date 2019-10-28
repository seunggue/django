from django import forms
from .models import Comment, Monster

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)