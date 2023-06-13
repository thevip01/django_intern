from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import JsonResponse, QueryDict
from django.core.paginator import Paginator

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
            return redirect('/job/all/')
        else:
            print(PrefResponse.errors, BasicResponse.errors)
            return HttpResponse(PrefResponse.errors, BasicResponse.errors)


orderBy = 'id'


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
    global pageNo
    fetchedData = BasicDetail.objects.all().order_by(orderBy)
    tableData = FormatData(fetchedData)

    return tableData


limit = 3


def showAll(request):
    tableData = DataGet()
    paginator = Paginator(tableData, limit)
    pageNo = request.GET.get('page')
    if (pageNo == None):
        pageNo = 1
    pageData = paginator.get_page(pageNo)
    return render(request, "Grid.html", {"context": pageData})


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
    return redirect('/job/all/')


def DeleteData(request, id):
    BasicDetail.objects.filter(id=id).delete()
    return redirect('/job/all/')


def SearchData(request, searchBy, searchVal):
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
    eduDataB = [eduData[i] for i in range(len(eduData))]
    expDataB = [expData[i] for i in range(len(expData))]
    refDataB = [refData[i] for i in range(len(refData))]
    TechLanguageDataB = [techLangData[i] for i in range(len(techLangData))]
    langDataB = [langData[i] for i in range(len(langData))]
    return JsonResponse({'Data': [{'BasicData': basicData[0]}, {'PreferenceData': prefData[0]}], 'MultipleData': [{'EducationData': eduDataB}, {'ExperienceData': expDataB},  {'ReferenceData': refDataB}], 'Language': [{
        'LanguageData': langDataB}, {'TechLanguageData': TechLanguageDataB},]})


def update(request, id):
    if request.POST:
        uID = BasicDetail.objects.get(pk=id)
        BasicResponse = BasicForm(request.POST, instance=uID)

        pid = preferenceDetail.objects.get(userID=id)
        PrefResponse = preferenceForm(request.POST, instance=pid)
        formResponese = dict(request.POST)

        if BasicResponse.is_valid() and PrefResponse.is_valid():
            BasicResponse.save()
            PrefResponse.save()
            edid = EducationDetail.objects.filter(userID=id)
            itemLen = len(formResponese['board_name'])
            for i in range(max(len(edid), itemLen)):
                if (i >= itemLen and i < len(edid)):
                    EducationDetail.objects.filter(id=edid[i].id).delete()
                else:
                    eduData = QueryDict(
                        f"board_name={formResponese['board_name'][i]}&passing_year={int(formResponese['passing_year'][i])}&percentage={int(formResponese['percentage'][i])}")
                    if (i < len(edid)):
                        EducationResponse = EducationForm(
                            eduData, instance=edid[i])
                        if (EducationResponse.is_valid()):
                            EducationResponse.save()
                        else:
                            print(EducationResponse.errors)

                    else:
                        EducationResponse = EducationForm(eduData)
                        if (EducationResponse.is_valid()):
                            edu = EducationResponse.save(commit=False)
                            edu.userID = uID
                            EducationResponse.save()
                        else:
                            print(EducationResponse.errors)

            exid = ExperienceDetail.objects.filter(userID=id)
            itemLen = len(formResponese['company_name'])
            for i in range(max(len(exid), itemLen)):
                if (i >= itemLen and i < len(exid)):
                    ExperienceDetail.objects.filter(id=exid[i].id).delete()
                else:
                    expeData = QueryDict(
                        f"company_name={formResponese['company_name'][i]}&ex_designation={formResponese['ex_designation'][i]}&from_date={formResponese['from_date'][i]}&to_date={formResponese['to_date'][i]}")

                    if (i < len(exid)):
                        ExperienceResponse = ExperienceForm(
                            expeData, instance=exid[i])
                        if (ExperienceResponse.is_valid()):
                            ExperienceResponse.save()
                        else:
                            print(ExperienceResponse.errors)
                    else:
                        ExperienceResponse = ExperienceForm(expeData)
                        if (ExperienceResponse.is_valid()):
                            exp = ExperienceResponse.save(commit=False)
                            exp.userID = uID
                            ExperienceResponse.save()
                        else:
                            print(ExperienceResponse.errors)

            rid = referenceDetail.objects.filter(userID=id)
            itemLen = len(formResponese['ref_name'])
            for i in range(max(len(rid), itemLen)):
                if (i >= itemLen and i < len(rid)):
                    referenceDetail.objects.filter(id=rid[i].id).delete()
                else:
                    refData = QueryDict(
                        f"ref_name={formResponese['ref_name'][i]}&ref_contact={int(formResponese['ref_contact'][i])}&ref_relation={formResponese['ref_relation'][i]}")
                    if (i < len(rid)):
                        ReferResponse = referenceForm(
                            refData, instance=rid[i])
                        if (ReferResponse.is_valid()):
                            ReferResponse.save()
                        else:
                            print(ReferResponse.errors)
                    else:
                        ReferResponse = referenceForm(refData)
                        if (ReferResponse.is_valid()):
                            ref = ReferResponse.save(commit=False)
                            ref.userID = uID
                            ReferResponse.save()
                        else:
                            print(ReferResponse.errors)

            lid = KnownLanguage.objects.filter(userID=id)
            itemLen = len(formResponese['language'])
            for i in range(max(len(lid), itemLen)):
                if (i >= itemLen and i < len(lid)):
                    KnownLanguage.objects.filter(id=lid[i].id).delete()
                else:
                    suffix_list = ''
                    for e in formResponese['expertise']:
                        for element in e.split():
                            if element.endswith(formResponese['language'][i]):
                                suffix_list += element.lower()[:-2] + ','
                    langData = QueryDict(
                        f"language={formResponese['language'][i]}&expertise={str(suffix_list)}")
                    if (i < len(lid)):
                        LanguageResponse = LanguageForm(
                            langData, instance=lid[i])
                        if (LanguageResponse.is_valid()):
                            LanguageResponse.save()
                        else:
                            print(LanguageResponse.errors)
                    else:
                        LanguageResponse = LanguageForm(langData,)
                        if (LanguageResponse.is_valid()):
                            lang = LanguageResponse.save(commit=False)
                            lang.userID = uID
                            LanguageResponse.save()
                        else:
                            print(LanguageResponse.errors)

            tlid = KnownTechLang.objects.filter(userID=id)
            itemLen = len(formResponese['techLanguage'])
            for i in range(max(len(tlid), itemLen)):
                if (i >= itemLen and i < len(tlid)):
                    KnownTechLang.objects.filter(id=tlid[i].id).delete()
                else:
                    techLangData = QueryDict(
                        f"techLanguage={formResponese['techLanguage'][i]}&techLangExpertise={formResponese[formResponese['techLanguage'][i]][0]}")
                    if (i < len(tlid)):
                        techLanguageResponse = TechLanugaeForm(
                            techLangData, instance=tlid[i])
                        if (techLanguageResponse.is_valid()):
                            techLanguageResponse.save()
                        else:
                            print(techLanguageResponse.errors)
                    else:
                        techLanguageResponse = TechLanugaeForm(techLangData)
                        if (techLanguageResponse.is_valid()):
                            techLang = techLanguageResponse.save(commit=False)
                            techLang.userID = uID
                            techLanguageResponse.save()
                        else:
                            print(techLanguageResponse.errors)

        else:
            print(PrefResponse.errors, BasicResponse.errors)

    return redirect('/job/all/')
