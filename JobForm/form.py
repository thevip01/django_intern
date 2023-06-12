from django import forms
from .models import BasicDetail, EducationDetail, ExperienceDetail, KnownLanguage, KnownTechLang, referenceDetail, preferenceDetail


class BasicForm(forms.ModelForm):
    class Meta:
        model = BasicDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'col-sm form-control my-1 mx-10'
        self.fields['address'].widget.attrs['rows'] = '1'


class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        exclude = ['id', 'userID',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'col-sm  my-1 mx-5'


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetail
        exclude = ['id', 'userID',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'col-sm my-1 mx-2'


class LanguageForm(forms.ModelForm):

    class Meta:
        model = KnownLanguage
        exclude = ['id', 'userID',]


class TechLanugaeForm(forms.ModelForm):
    class Meta:
        model = KnownTechLang
        exclude = ['id', 'userID',]


class referenceForm(forms.ModelForm):
    class Meta:
        model = referenceDetail
        exclude = ['id', 'userID']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'col-sm  my-1 mx-5 classRef'


class preferenceForm(forms.ModelForm):
    class Meta:
        model = preferenceDetail
        exclude = ['id', 'userID']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'col-sm la'
            self.fields['pref_loaction'].widget = forms.SelectMultiple()
            self.fields['pref_department'].widget = forms.SelectMultiple()
