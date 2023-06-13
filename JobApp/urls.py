from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='job/')),
    path('admin/', admin.site.urls),
    path('job/', include('JobForm.urls')),
    path('task/', include('classviewex.urls')),
]
