from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from patients.models import patients, patient_characteristic

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
    patient_id = int(request.GET.get('pid'))
    print("pid = " + str(patient_id))
    context = {
        'patient': patients.objects.filter(pid = patient_id).first(),
        'patient_info': list(patient_characteristic.objects.filter(pid = patient_id))
    }
    return render(request, 'patient_info.html', context)
