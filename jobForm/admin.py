from django.contrib import admin

from .models import JobDetailTable
from .models import UserRegisterModel

admin.site.register(JobDetailTable)
admin.site.register(UserRegisterModel)
