from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse

from .myForm import JobAppForm
from .models import JobDetailTable


def home(request):
    return render(request, 'MainHome.html')


def JobForm(request):
    FormResponse = JobAppForm(request.POST or None)
    if FormResponse.is_valid():
        FormResponse.save()

    return render(request, 'JobApp.html', {"FormResponse": FormResponse})


orderBy = 'id'


def JobAppDetail(request):
    userData = JobDetailTable.objects.order_by(orderBy)
    return render(request, 'userFormDetails.html', {'userData': userData, 'isSorted': orderBy})


def delete(request, id):
    deleteQ = JobDetailTable.objects.get(id=id)
    deleteQ.delete()
    return redirect(reverse('JobForm:userData'))


def update(request, id):
    query = JobDetailTable.objects.get(id=id)
    updateQ = JobAppForm(request.POST or None, instance=query)
    if updateQ.is_valid():
        updateQ.save()
    return render(request, 'JobApp.html', {"FormResponse": updateQ})


def SortData(request, sortName):
    global orderBy
    if (orderBy == sortName):
        orderBy = f'-{sortName}'
    elif (orderBy == f'-{sortName}'):
        orderBy = 'id'
    else:
        orderBy = sortName
    return redirect(reverse('JobForm:userData'))
