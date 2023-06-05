from django.forms import ModelForm

from .models import JobDetailTable


class JobAppForm(ModelForm):
    class Meta:
        model = JobDetailTable
        exclude = ['id',]
