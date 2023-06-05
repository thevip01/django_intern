from django.shortcuts import render, redirect, reverse

from .BasicDetailForm import BasicForm, EducationForm
from .BasicDetailForm import ExperienceForm, ReferenceForm, LanguageForm, LangExperticeForm


def JobForm(request):
    userBasicForm = BasicForm()
    userEducationForm = EducationForm()
    userExperienceForm = ExperienceForm()
    userReferenceForm = ReferenceForm()
    userLanguageForm = LanguageForm()
    userLangExpertice = LangExperticeForm()
    return render(request, 'JobForm.html', {'BasicDetail': userBasicForm, 'EducationDetail': userEducationForm, 'ExperienceDetail': userExperienceForm, 'ReferenceDetail': userReferenceForm, 'LanguageDetail': userLanguageForm, 'LangExpertice': userLangExpertice})
