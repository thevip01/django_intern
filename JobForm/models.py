from django.db import models

GenderChoice = [
    ('male', 'Male'),
    ('female', 'Female'),
]

RelationshipChoice = [
    ('married', 'Married'),
    ('unmarried', 'Unmarried'),
]

# Create your models here.


class allState(models.Model):
    stateName = models.CharField(max_length=90)

    def __str__(self):
        return self.stateName


class cities(models.Model):
    state_id = models.ForeignKey(
        allState, on_delete=models.CASCADE)
    city = models.CharField(max_length=90)


class Language(models.Model):
    language = models.CharField(max_length=90)

    def __str__(self):
        return self.language


class TechLanguages(models.Model):
    TechLanguageName = models.CharField(max_length=255)

    def __str__(self):
        return self.TechLanguageName


class BasicDetail(models.Model):
    firstname = models.CharField(
        "First Name", max_length=80,  blank=False, null=False)
    lastname = models.CharField(
        "Last Name", max_length=80,  blank=False, null=False)
    email = models.CharField("Email", max_length=20,  blank=False, null=False)
    phone = models.IntegerField("Phone Number",  blank=False, null=False)
    designation = models.CharField(
        "Designation", max_length=80,  blank=False, null=False)
    gender = models.CharField(choices=GenderChoice,
                              max_length=90,  blank=False, null=False)
    relationship_status = models.CharField(
        choices=RelationshipChoice, max_length=90, blank=False, null=False)
    dob = models.DateField('Date Of Birth',  blank=False, null=False)
    address = models.TextField(
        "Address", max_length=200,  blank=False, null=False)
    state = models.ForeignKey(
        allState, on_delete=models.CASCADE,  blank=False, null=False)
    city = models.CharField("City", max_length=30,
                            blank=False, null=False)
    zipcode = models.IntegerField("Zip Code", blank=False, null=False)

    def __str__(self):
        return str(self.id)


class EducationDetail(models.Model):
    userID = models.ForeignKey(
        BasicDetail,
        on_delete=models.CASCADE
    )
    board_name = models.CharField("Name of board", max_length=90)
    percentage = models.IntegerField("Percentages")
    passing_year = models.IntegerField("Passing Year")


class ExperienceDetail(models.Model):
    userID = models.ForeignKey(
        BasicDetail,
        on_delete=models.CASCADE
    )
    company_name = models.CharField("Company Name", max_length=90)
    ex_designation = models.CharField("Designation",  max_length=50)
    from_date = models.DateField("From")
    to_date = models.DateField("To")


class KnownLanguage(models.Model):
    userID = models.ForeignKey(
        BasicDetail,
        on_delete=models.CASCADE
    )
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=255)


class KnownTechLang(models.Model):
    userID = models.ForeignKey(BasicDetail, on_delete=models.CASCADE)
    techLanguage = models.ForeignKey(TechLanguages, on_delete=models.CASCADE)
    techLangExpertise = models.CharField(max_length=90)


class referenceDetail(models.Model):
    userID = models.ForeignKey(BasicDetail, on_delete=models.CASCADE)
    ref_name = models.CharField("Name", max_length=100)
    ref_contact = models.IntegerField("Contact")
    ref_relation = models.CharField("Relation", max_length=100)


class preferenceDetail(models.Model):

    available_Locations = [
        ('ahmedabad', 'Ahmedabad'),
        ('palanpur', 'Palanpur'),
        ('surat', 'Surat'),
        ('rajkot', 'Rajkot'),
    ]

    departments = [
        ('marketing', 'Marketing'),
        ('management', 'Management'),
        ('devlopment', 'Devlopment'),
        ('design', 'Design'),
    ]

    userID = models.ForeignKey(BasicDetail, on_delete=models.CASCADE)

    pref_loaction = models.CharField(
        'Location', max_length=255, choices=available_Locations)

    notice_period = models.IntegerField("Notice Period")
    expected_ctc = models.CharField("Expected CTC", max_length=255)
    current_ctc = models.CharField("Current CTC", max_length=255)
    pref_department = models.CharField(
        "Department", max_length=255, choices=departments)
