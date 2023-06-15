from django.contrib import admin
from .models import subject, student, faculty, department
# Register your models here.
admin.site.register(subject)
admin.site.register(student)
admin.site.register(faculty)
admin.site.register(department)
