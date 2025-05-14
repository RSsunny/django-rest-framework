from django.db import models

# Create your models here.
class Teacher(models.Model):
    name= models.CharField(max_length=100)
    subject= models.CharField(max_length=100)
    time= models.TimeField()
    date= models.DateField()
    phone= models.CharField(max_length=15)
    email= models.EmailField()
    address= models.TextField()
    