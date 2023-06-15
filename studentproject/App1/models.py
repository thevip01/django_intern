from django.db import models

# Create your models here.


class subject(models.Model):
    subject_name = models.CharField(null=False, max_length=90)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name


class student(models.Model):
    name = models.CharField(max_length=90)
    subject_name = models.ManyToManyField(
        subject,  related_name='subject_student')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class faculty(models.Model):
    name = models.CharField(max_length=90)
    subject_name = models.ManyToManyField(
        subject,  related_name='subject_faculty', through='department')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class department(models.Model):
    faculty_name = models.ForeignKey(
        faculty, on_delete=models.CASCADE, null=False)
    subject_name = models.ForeignKey(
        subject, on_delete=models.CASCADE, null=False)

    # class Meta:
    #     unique_together = [['faculty_name', 'subject_name']]
