from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'JobApp'
urlpatterns = [
    path('', views.JobForm, name='JobApplicationForm'),
    path('getcity/<int:id>', views.getusercity, name='getcity'),
    path('apply/', views.ApplyForm, name='Apply'),
    path('all/', views.showAll, name='AllGrid'),
    path('sort/<str:sortName>', views.SortData, name='sort'),
    path('edit/<int:id>', views.JobForm, name='edit'),
    path('getData/<int:id>', views.EditForm, name='EditForm'),
    path('delete/<int:id>', views.DeleteData, name='delete'),
    path('search/<str:searchBy>/<str:searchVal>',
         views.SearchData, name='search'),
    path('update/<int:id>', views.update, name='update'),

]
