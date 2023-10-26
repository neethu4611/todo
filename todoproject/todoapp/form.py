from . models import task
from django import forms
class todo_form(forms.ModelForm):
    class Meta():
        model=task
        fields=['name','priority','date']