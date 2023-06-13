from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    TaskName = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}), label="Task")

    class Meta:
        model = Task
        fields = '__all__'
