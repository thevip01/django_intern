from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'classView'
urlpatterns = [
    path('', views.TaskList.as_view(), name='TaskList'),
    path('delete/<int:id>', views.TaskDelete.as_view(), name='delete'),
    path('edit/<int:id>', views.TaskEdit.as_view(), name='edit')
]
