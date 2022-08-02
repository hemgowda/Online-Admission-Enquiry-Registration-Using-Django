import email
from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    qualifying_exam = models.CharField(max_length=50)
    rank = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    def __str__(self):
        return self.name
   
class Department(models.Model):
    D_name = models.CharField(max_length=30)
    D_loction = models.CharField(max_length=50)
    start_year = models.IntegerField(max_length=4)
    intake = models.IntegerField()
    def __str__(self):
        return self.D_name
class Admission(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return self.date

