from django import forms
from django.forms import ModelForm, Textarea
from .models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder': "Add a new task..."}))
    
    class Meta:
        model = Task
        fields = ['title', 'complete'] # or '__all__' will be okay because on template, input box has beeb particulary specified
        