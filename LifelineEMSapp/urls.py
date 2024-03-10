from django.urls import path
from django.urls import re_path as url
from . import views

app_name = 'LifelineEMSapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
     path('login/', views.login, name='login'),
     path('admind/', views.admind, name='admind'),
     path('student/', views.student, name='student'),
     path('staff/', views.student, name='staff'),
     path('cashier/', views.cashier, name='cashier'),
      path('register/', views.register, name='register'),

]