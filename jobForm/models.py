from django.db import models


class JobDetailTable(models.Model):
    firstName = models.CharField(
        'First Name', max_length=80, blank=False, null=False)
    lastName = models.CharField(
        'Last Name', max_length=80, blank=False, null=False)
    email = models.EmailField('Email', max_length=80, blank=False, null=False)
    phoneNumber = models.IntegerField(
        'Phone Number', blank=False, null=False)
    dob = models.DateField('Date of Birth', null=False)
