import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from django.urls import reverse
from .forms import Studentform
# Create your views here.
def index(request):
    return render(request,'student/index.html',{
        'students':Student.objects.all()})

def view_student(request,id):
    student =Student.objects.get(pk=id)    
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method=='POST':
        form=Studentform(request.POST)
        if form.is_valid():
            new_mobile_no= form.cleaned_data['mobile_no']
            new_student_fname=form.cleaned_data['student_fname']
            new_student_lname=form.cleaned_data['student_lname']
            new_email=form.cleaned_data['email']
            new_aadhar_no=form.cleaned_data['aadhar_no']
            new_college_registerid=form.cleaned_data['college_registerid']
            
            new_student=Student(student_fname=new_student_fname,
                                student_lname=new_student_lname,
                                email=new_email,
                                mobile_no=new_mobile_no,
                                aadhar_no=new_aadhar_no,
                                college_registerid=new_college_registerid)
            new_student.save()
            return render(request,'student/add.html',{
                          'form':Studentform(),
                          'Success':True})
    else:
        return render(request,'student/add.html',
                      {'form':Studentform()})        