from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('home/', views.home, name='home'),
    path('SendApplication/', views.userApply , name='userApply'),
]