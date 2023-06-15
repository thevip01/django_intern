from .models import *


import random
from faker import Faker
fake = Faker()


def add_faker(n):
    try:
        courses = courseDB.objects.all()
        for _ in range(n):
            r = random.randint(0, len(courses)-1)
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 30)
            student_address = fake.address()
            course = courses[r]

            student.objects.create(
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
                course=course,
            )
    except Exception as e:
        print(e)
