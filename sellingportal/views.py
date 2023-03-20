from django.shortcuts import render
from django.http import HttpResponse
from sellingportal import models
from sellingportal import forms

def Index(request):
    context={'name': 'Hamid',
             'age': 25,
             'jobs': ['eng', 'lecture', 'dev']
             }
    return render(request, 'index.html', context)
    #return HttpResponse('Welcome to index page')


def Student(request):
    students=models.Student.objects.all()
    context={
            'students':students
    }
    return render(request,'students.html',context)



def Register(request):
    form_data=forms.UserRegistrar(request.POST or None)
    msg=''
    if form_data.is_valid():
        student=models.Student()
        student.first_name=form_data.cleaned_data['first_name']
        student.last_name=form_data.cleaned_data['last_name']
        student.age=form_data.cleaned_data['age']
        student.date_birth=form_data.cleaned_data['date_birth']
        student.save()
        msg='data is saved'

    context={'formregister':form_data,
            'msg':msg
             }
    return render(request, 'regiester.html', context)


def StuDgree(request,student_id):
    degrees=models.Degree.objects.filter(student_id=student_id)
    students=models.Student.objects.get(id=student_id)
    form_data=forms.DegreeRegistrar(request.POST or None)
    msg=''
    if form_data.is_valid():
        degree=models.Degree()
        degree.student_degree=form_data.cleaned_data['student_degree']
        degree.student_id=students
        degree.save()
        msg='data is saved'
    context={
            'degrees':degrees,
            'formregister':form_data,
            'msg':msg
    }
    return render(request,'degrees.html',context)

def Home(request):
    return render(request,'home.html')

def Insc(request):
    return render(request,'insc.html')