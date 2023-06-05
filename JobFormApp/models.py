from django.db import models

StateChoice = [
    ('gujarat', 'Gujarat'),
    ('maharastra', 'Maharastra'),
    ('uttarpradesh', 'UttarPradesh'),
    ('rajastan', 'Rajastan'),
]

GenderChoice = [
    ('male', 'Male'),
    ('female', 'Female'),
]

RelationshipChoice = [
    ('married', 'Married'),
    ('unmarried', 'UnMarried'),
]

LanguageExpert = RelationshipChoice = [
    ('read', 'Read'),
    ('write', 'Write'),
    ('speak', 'Speak'),
]


class BasicDetail(models.Model):
    firstname = models.CharField("First Name", max_length=80)
    lastname = models.CharField("Last Name", max_length=80)
    designation = models.CharField("Designation", max_length=80)
    address = models.TextField("Address", max_length=200)
    email = models.CharField("Email", max_length=20)
    city = models.CharField("City", max_length=30)
    phone = models.IntegerField("Phone Number")
    state = models.CharField("State", choices=StateChoice, max_length=90)
    gender = models.CharField(choices=GenderChoice, max_length=90)
    zipcode = models.IntegerField("Zip Code")
    relationship_status = models.CharField(
        choices=RelationshipChoice, max_length=90)
    dob = models.DateField('Date Of Birth')


class EducationDetail(models.Model):
    # userId = models.ForeignKey(BasicDetail, on_delete=models.PROTECT, blank=False)
    boardname = models.CharField("Name of board", max_length=90)
    passingyear = models.DateField("Passing Year")
    percentage = models.IntegerField("Percentages")


class ExperienceDetail(models.Model):
    # userId = models.ForeignKey(BasicDetail, on_delete=models.PROTECT, blank=False)
    companyname = models.CharField("Company Name", max_length=90)
    designation = models.CharField("Designation",  max_length=50)
    fromdate = models.DateField("From")
    todate = models.DateField("To")


class ReferenceDetail(models.Model):
    # userId = models.ForeignKey(BasicDetail, on_delete=models.PROTECT, blank=False)
    name = models.CharField("Name", max_length=90)
    conatctno = models.IntegerField("Contact Number")
    relation = models.CharField("Relation", max_length=30)


class LanguagesDetail(models.Model):
    # userId = models.ForeignKey(BasicDetail, on_delete=models.PROTECT, blank=False)
    hindi = models.CharField('Hindi', max_length=90)
    english = models.CharField('English', max_length=90)
    gujarati = models.CharField('Gujarati', max_length=90)


class LanguageExpertice(models.Model):
    expertice = models.CharField(choices=LanguageExpert, max_length=90)
