from django.shortcuts import render
from . import models
from .models import Patients
from django.views.generic import CreateView
from django.http import HttpResponse


# Create your views here.

def homepage(request):
    Patients = models.Patients.objects.all()
    return render(request, 'TMH/Home.html', {} )
    

def home(request):
    Patients = models.Patients.objects.all()
    return render(request, 'TMH/details.html',{'Patients':Patients})

def about(request):
    return render(request,'TMH/about.html',{})

def details(request):
    if request.method =='POST':
        id1_value = request.POST.get('id1')
        id2_value = request.POST.get('id2')
        id3_value = request.POST.get('id3')
        id4_value = request.POST.get('id4')
        id5_value = request.POST.get('id5')
        id6_value = request.POST.get('id6')
        id7_value = request.POST.get('id7')
        id8_value = request.POST.get('id8')
        id9_value = request.POST.get('id9')
        ida_value = request.POST.get('ida')

        Patients.objects.Create(id1 = id1_value,id2 = id2_value,id3 = id3_value,id4 = id4_value,id5 = id5_value,id6= id6_value,id7 = id7_value,id8 = id8_value,id9= id9_value,ida = ida_value)

        return HttpResponse('submitted')



class PatientsCreateView(CreateView):
    model = Patients
    fields = ['EntryDate',
        'PatientID' ,
        'PatientName',
        'Sex',
        'DOB',
        'HospitalVisited',
        'Illness',
        'MedicalTest',
        'Treatment' ,
        'Contact',
        'Address']

    success_url = 'details'
