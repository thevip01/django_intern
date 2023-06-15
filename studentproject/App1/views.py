from django.shortcuts import render, HttpResponse
from django.views import View
from .models import subject, student, faculty

# Create your views here.


class DataView(View):
    def get(self, request):
        Veer = student.objects.get(id=1)
        subjects = Veer.subject_name.all()

        Physics = subject.objects.get(id=1)
        stu1 = Physics.subject_student.all()

        Raghav = faculty.objects.get(id=1)
        subject1 = Raghav.subject_name.all()

        fac1 = Physics.subject_faculty.all()

        return HttpResponse(f'''Student : {Veer.name} ---> Subjects : {[i.subject_name for i in subjects]} <br>
                             Subject : {Physics} ---> Students : {[i.name for i in stu1]}<br><br><br>
                             Faculty : {Raghav.name} ---> Subjects : {[i.subject_name for i in subject1]} <br>
                             Subject : {Physics} ---> Faculty : {[i.name for i in fac1]}<br><br><br>
                             ''')
        # subject
        # department
        # faculty, student
