from django.contrib import admin

from .models import allState, Language, TechLanguages, BasicDetail, cities, EducationDetail, ExperienceDetail, KnownLanguage, KnownTechLang, referenceDetail, preferenceDetail
# Register your models here.

admin.site.register(allState)
admin.site.register(cities)
admin.site.register(Language)
admin.site.register(TechLanguages)
admin.site.register(BasicDetail)
admin.site.register(EducationDetail)
admin.site.register(ExperienceDetail)
admin.site.register(KnownLanguage)
admin.site.register(KnownTechLang)
admin.site.register(referenceDetail)
admin.site.register(preferenceDetail)
