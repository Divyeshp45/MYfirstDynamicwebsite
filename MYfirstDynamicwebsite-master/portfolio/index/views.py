from django.shortcuts import render
from index.models import Feedback
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def feedback(request):
    if request.method=="POST":
        user_pass=request.POST["exampleInputPassword1"]
        email=request.POST["exampleInputEmail1"]
        obj=Feedback(email=email,user_pass=user_pass)
        obj.save()
    return render(request,'feedback.html')