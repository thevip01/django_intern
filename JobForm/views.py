from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, QueryDict
import json
from django.core.serializers import serialize

from .form import BasicForm, EducationForm, ExperienceForm, LanguageForm, TechLanugaeForm, referenceForm, preferenceForm
from .models import cities, Language, TechLanguages, BasicDetail, EducationDetail, ExperienceDetail, KnownLanguage, KnownTechLang, referenceDetail, preferenceDetail

# Create your views here.


def JobForm(request, id=''):
    userBasicForm = BasicForm()
    userEducationForm = EducationForm()
    userExperienceForm = ExperienceForm()

    userLanguage = Language.objects.all()
    userTechLanugae = TechLanguages.objects.all()

    userReferenceForm = referenceForm()
    userPreferenceForm = preferenceForm()
    return render(request, 'JobForm.html', {'form': [userBasicForm, userEducationForm, userExperienceForm, userLanguage, userTechLanugae, userReferenceForm, userPreferenceForm], 'id': id})


def getusercity(request, id):
    objectResposne = cities.objects.filter(state_id=id).values_list()
    citiesResponse = [objectResposne[i] for i in range(len(objectResposne))]
    return JsonResponse({'cities': citiesResponse})


def ApplyForm(request):
    if request.POST:
        BasicResponse = BasicForm(request.POST)
        PrefResponse = preferenceForm(request.POST)
        formResponese = dict(request.POST)
        if BasicResponse.is_valid() and PrefResponse.is_valid():
            uID = BasicResponse.save()
            for i in range(len(formResponese['board_name'])):
                eduData = QueryDict(
                    f"board_name={formResponese['board_name'][i]}&passing_year={int(formResponese['passing_year'][i])}&percentage={int(formResponese['percentage'][i])}")

                EducationResponse = EducationForm(eduData)
                if (EducationResponse.is_valid()):
                    edu = EducationResponse.save(commit=False)
                    edu.userID = uID
                    EducationResponse.save()
                else:
                    print(EducationResponse.errors)

            for i in range(len(formResponese['company_name'])):
                expeData = QueryDict(
                    f"company_name={formResponese['company_name'][i]}&ex_designation={formResponese['ex_designation'][i]}&from_date={formResponese['from_date'][i]}&to_date={formResponese['to_date'][i]}")

                ExperienceResponse = ExperienceForm(expeData)
                if (ExperienceResponse.is_valid()):
                    exp = ExperienceResponse.save(commit=False)
                    exp.userID = uID
                    ExperienceResponse.save()
                else:
                    print(ExperienceResponse.errors)

            for i in range(len(formResponese['ref_name'])):
                refData = QueryDict(
                    f"ref_name={formResponese['ref_name'][i]}&ref_contact={int(formResponese['ref_contact'][i])}&ref_relation={formResponese['ref_relation'][i]}")

                ReferResponse = referenceForm(refData)
                if (ReferResponse.is_valid()):
                    ref = ReferResponse.save(commit=False)
                    ref.userID = uID
                    ReferResponse.save()
                else:
                    print(ReferResponse.errors)

            for item in formResponese['language']:
                suffix_list = ''
                for e in formResponese['expertise']:
                    for element in e.split():
                        if element.endswith(item):
                            suffix_list += element.lower()[:-2] + ','
                langData = QueryDict(
                    f"language={item}&expertise={str(suffix_list)}")
                LanguageResponse = LanguageForm(langData)
                if (LanguageResponse.is_valid()):
                    lang = LanguageResponse.save(commit=False)
                    lang.userID = uID
                    LanguageResponse.save()
                else:
                    print(LanguageResponse.errors)

            for item in formResponese['techLanguage']:
                techLangData = QueryDict(
                    f"techLanguage={item}&techLangExpertise={formResponese[item][0]}")
                techLanguageResponse = TechLanugaeForm(techLangData)
                if (techLanguageResponse.is_valid()):
                    techLang = techLanguageResponse.save(commit=False)
                    techLang.userID = uID
                    techLanguageResponse.save()
                else:
                    print(techLanguageResponse.errors)

            pref = PrefResponse.save(commit=False)
            pref.userID = uID
            PrefResponse.save()
            return redirect('JobApp')
        else:
            print(PrefResponse.errors, BasicResponse.errors)
        return HttpResponse('ERROR')


orderBy = 'id'
limit = 2
offset = 0


def FormatData(fetchedData):
    tableData = []
    for item in fetchedData:
        gridData = {}

        gridData['id'] = item.id
        gridData['name'] = item.firstname
        gridData['phoneNo'] = item.phone
        gridData['email'] = item.email
        gridData['designation'] = item.designation

        tableData.append(gridData)
    return tableData


def DataGet():
    fetchedData = BasicDetail.objects.all().order_by(orderBy)[
        offset:offset+limit]
    tableData = FormatData(fetchedData)

    return tableData


def showAll(request, pageno=1):
    global offset
    offset = limit*(pageno-1)
    tableData = DataGet()
    count = BasicDetail.objects.all().count()
    pages = count/limit
    return render(request, "Grid.html", {'context': tableData, 'count': range(int(pages)+1), 'isSorted': orderBy})


def SortData(request, sortName):
    global orderBy
    if sortName == 'name':
        sortName = 'firstname'
    elif sortName == 'phoneNo':
        sortName = 'phone'
    if (orderBy == sortName):
        orderBy = f'-{sortName}'
    elif (orderBy == f'-{sortName}'):
        orderBy = 'id'
    else:
        orderBy = sortName
    return redirect('/job/all/1')


def DeleteData(request, id):
    BasicDetail.objects.filter(id=id).delete()
    return redirect('/job/all/1')


def SearchData(request, searchBy, searchVal):
    print(searchBy, searchVal)
    if (searchBy == 'name'):
        searchData = BasicDetail.objects.filter(firstname=searchVal)
    elif searchBy == 'id':
        searchData = BasicDetail.objects.filter(id=searchVal)
    elif searchBy == 'designation':
        searchData = BasicDetail.objects.filter(designation=searchVal)
    return JsonResponse({'searchData': FormatData(searchData)})


def EditForm(request, id):
    basicData = BasicDetail.objects.filter(id=id).values()
    eduData = EducationDetail.objects.filter(userID=id).values()
    expData = ExperienceDetail.objects.filter(userID=id).values()
    langData = KnownLanguage.objects.filter(userID=id).values()
    techLangData = KnownTechLang.objects.filter(userID=id).values()
    refData = referenceDetail.objects.filter(userID=id).values()
    prefData = preferenceDetail.objects.filter(userID=id).values()
    return JsonResponse({'Data': [{'BasicData': basicData[0]}, {'EducationData': eduData[0]}, {'ExperienceData': expData[0]}, {
        'LanguageData': langData[0]}, {'TechLanguageData': techLangData[0]}, {'ReferenceData': refData[0]}, {'PreferenceData': prefData[0]}]})
