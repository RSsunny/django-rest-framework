from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
  path('ts/', views.teacher_list, name='teacher_list'),
  path('ts/<int:id>', views.SingleTeacher, name='SingleTeacher'),
  path('ts_create/', views.teacher_create, name='teacher_create')
]
