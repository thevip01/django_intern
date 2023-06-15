from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *
# Create your views here.


class DataView(View):
    def get(self, request):
        obj = student.objects.filter(course__course_name__icontains="CE")
        print(obj[0].course.course_name)
        return HttpResponse('')
