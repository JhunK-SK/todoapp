from django import forms
from django.forms import ModelForm, Textarea
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'complete']
        # widgets = {
        #     'title': Textarea(attrs={'cols':80, 'rows':10}),
        #     }