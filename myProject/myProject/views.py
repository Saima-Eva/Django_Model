from django.shortcuts import render
from myapp.models import *

def studentPage(request):
    student = Student_Model.objects.all()
    
    context = {
        "std": student,
    }
    
    return render(request,"student.html",context)


def teacherPage(request):
    teacher = Teachers_Model.objects.all()
    
    context = {
        "tch": teacher,
    }
    
    return render(request,"teacher.html",context)


def employeePage(request):
    employee = Employee_Model.objects.all()
    
    context = {
        "emp": employee,
    }
    
    return render(request,"employee.html",context)