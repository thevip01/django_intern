from django.db import models

# Create your models here.


class courseDB(models.Model):
    course_name = models.CharField(max_length=200)


class student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    student_age = models.IntegerField()
    student_address = models.CharField(max_length=255)
    course = models.ForeignKey(
        courseDB, on_delete=models.CASCADE, related_name='course_nm')
