from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'body']



