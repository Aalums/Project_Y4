from django.contrib import admin
from patients.models import patient_characteristic, patient_mpi, patients
# Register your models here.

admin.site.register(patients)
admin.site.register(patient_mpi)
admin.site.register(patient_characteristic)
