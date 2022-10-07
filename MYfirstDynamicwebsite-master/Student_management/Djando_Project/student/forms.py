from cProfile import label
from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Student

class Studentform(forms.ModelForm):
    class Meta:
        model= Student
        fields =['mobile_no',
                  'student_fname',
                  'student_lname',
                  'email',
                  'aadhar_no',
                  'college_registerid',]
        labels={'mobile_no':"Mobile Number",
                  'student_fname':"First Name",
                  'student_lname':"Last Name",
                  'email':"EmailId",
                  'aadhar_no':"UID No",
                  'college_registerid':"Registered CollegeID",}
        widgets ={'mobile_no':forms.NumberInput(attrs={'class':'form-control'}),
                  'student_fname':forms.TextInput(attrs={'class':'form-control'}),
                  'student_lname':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'}),
                  'aadhar_no':forms.NumberInput(attrs={'class':'form-control'}),
                  'college_registerid':forms.NumberInput(attrs={'class':'form-control'}),}