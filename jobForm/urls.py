from django.urls import path

from . import views

app_name = 'JobForm'
urlpatterns = [
    path('', views.home, name='dbHome'),
    path('register/', views.UserRegistration, name='register'),
    path('registerPost/', views.userRegPost, name='registerPost'),
    path('JobApp/', views.JobForm, name='JobApp'),
    path('users/', views.JobAppDetail, name='userData'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.update, name='edit'),
    path('sort/<str:sortName>', views.SortData, name='sort'),
]
