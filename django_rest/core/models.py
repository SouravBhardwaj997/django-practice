from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.name

class Teacher(models.Model):
    emp_id= models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name