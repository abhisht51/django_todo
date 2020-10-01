from .models import TodoItem
from django.forms import ModelForm
from django import forms



class updateForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = '__all__'
        widgets = {
                'content' : forms.TextInput(attrs={'placeholder' : 'content'}),}