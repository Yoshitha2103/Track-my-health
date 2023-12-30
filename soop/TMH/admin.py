from django.contrib import admin
from . import models

# Register your models here.
class patientsAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Patients, patientsAdmin)