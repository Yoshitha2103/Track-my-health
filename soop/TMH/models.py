from django.db import models

# Create your models here.
class Patients(models.Model):
    EntryDate = models.DateField() 
    PatientID = models.PositiveIntegerField() 
    PatientName = models.CharField(max_length=20) 
    Sex = models.CharField(max_length=1)
    DOB = models.DateField()
    HospitalVisited = models.CharField(max_length=20) 
    Illness = models.CharField(max_length=20) 
    MedicalTest =models.CharField(max_length=20)  
    Treatment = models.CharField(max_length=20) 
    Contact =models.PositiveIntegerField() 
    Address = models.CharField(max_length=20) 

    