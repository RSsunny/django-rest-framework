from django.urls import path 
from . import views
urlpatterns = [
  path('ts_create', views.teacher_create, name='teacher_create'),
  path('ts_create/<int:id>', views.teacher_create, name='SingleTeacher'),
]
