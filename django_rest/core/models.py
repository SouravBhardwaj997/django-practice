from django.db import models

# Create your models here.

class Students(models.Model):
    stu_id = models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    dept= models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Teachers(models.Model):
    emp_id= models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name