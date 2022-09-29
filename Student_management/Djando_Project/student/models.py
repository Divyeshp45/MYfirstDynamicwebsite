from django.db import models


# Create your models here.
class Student(models.Model):
    student_fname=models.CharField(max_length=30)
    student_lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    mobile_no=models.PositiveIntegerField()
    aadhar_no=models.PositiveIntegerField()
    college_registerid=models.PositiveIntegerField()
    
    def __str__(self):
        return f"Student: {self.student_fname} {self.student_lname}"
    
    