from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from patients.models import patients

# Create your views here.
def addpatient(request):
    header_str = 'Hello'
    template = loader.get_template('addpatient.html')
    context = {
        'var1': header_str
    }
    return HttpResponse(template.render(context, request))

def patientList(request):
    context = {
        'list_patient': list(patients.objects.all())
    }
    return render(request, 'patient_list.html', context)

def patientInfo(request):
    header_str = 'Hello'
    template = loader.get_template('patient_info.html')
    context = {
        'var1': header_str
    }
    return HttpResponse(template.render(context, request))
