from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.shortcuts import redirect, render, reverse
import json


def index(request):
    return render(request, 'form.html')


@csrf_exempt
def userApply(request):
    if request.method == "POST":
        tempInit = dict(request.POST)
        temp = '{' + \
            f'"name":"{tempInit["name"][0]}","email": "{tempInit["email"][0]}","remote":"{tempInit["remote"][0]}"'+'}'
        f = open('Data.txt', 'a')
        f.write(f"\n{temp}")
        f.close()
        return render(request, 'ApplyNew.html')


def home(request):
    f = open('Data.txt', 'r')
    len1 = len(f.readlines())
    Data1 = []
    f.close()
    f1 = open('Data.txt', 'r')
    for i in range(len1):
        l1 = f1.readline()
        Data1.append(json.loads(l1))
    f1.close()
    return render(request, 'userData1.html', {"Data": Data1})


def delete(request, id):
    f = open('Data.txt', 'r')
    Data = f.readlines()
    f.close()
    with open('Data.txt', 'w') as f1:
        f1.write('')
    f2 = open('Data.txt', 'a')
    for i in range(0, len(Data)):
        if i != id-1:
            print(Data[i])
            f2.write(Data[i])
    f2.close()

    return redirect('/form/home/')
