from django.db import models

# Create your models here.

class Student_Model(models.Model):
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    
class Teachers_Model(models.Model):
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    

class Employee_Model(models.Model):
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name+" "+self.last_name