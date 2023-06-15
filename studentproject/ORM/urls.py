from django.urls import path
from . import views

app_name = 'ORM_Test'
urlpatterns = [
    path('', views.DataView.as_view(), name=""),
]
