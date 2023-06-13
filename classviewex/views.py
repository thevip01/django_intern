from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from django.http import QueryDict

from .form import TaskForm
from .models import Task
# Create your views here.


class TaskList(View):
    def get(self, request):
        myTaskList = Task.objects.all()
        TaskData = []
        for item in myTaskList:
            TaskData.append({'id': item.id, 'TaskName': item.TaskName})
        form = TaskForm()
        return render(request, 'ToDo.html', {'form': form,  'Tasks': TaskData})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('classView:TaskList'))


class TaskDelete(View):

    def get(self, request, id):
        a = Task.objects.filter(id=id).delete()
        return redirect(reverse('classView:TaskList'))


class TaskEdit(View):
    def get(self, request, id):
        DataSet = Task.objects.get(id=id)
        form = TaskForm(QueryDict(f'TaskName={DataSet.TaskName}'))
        return render(request, 'ToDo.html', {'form': form, 'id': id})

    def post(self, request, id):
        TaskID = Task.objects.get(pk=id)
        form = TaskForm(request.POST, instance=TaskID)
        if form.is_valid():
            form.save()
            return redirect(reverse('classView:TaskList'))
