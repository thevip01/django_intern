from django import forms
from .models import BasicDetail, EducationDetail, ExperienceDetail, ReferenceDetail, LanguagesDetail, LanguageExpertice


class BasicForm(forms.ModelForm):
    class Meta:
        model = BasicDetail
        exclude = ['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        exclude = ['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetail
        exclude = ['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = ReferenceDetail
        exclude = ['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LanguageForm(forms.ModelForm):
    class Meta:
        model = LanguagesDetail
        exclude = ['id',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


LanguageExpert = RelationshipChoice = [
    ('read', 'Read'),
    ('write', 'Write'),
    ('speak', 'Speak'),
]


class LangExperticeForm(forms.ModelForm):
    expertice = forms.MultipleChoiceField(
        choices=LanguageExpert)

    class Meta:
        model = LanguageExpertice
        fields = '__all__'
