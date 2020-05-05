from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import patients, patient_info

# Create your views here.
def addpatient(request):
    if request.method == 'POST':
        patient = patients()
        patient.HN = request.POST.get('HN_number')
        patient.fname = request.POST.get('firstName')
        patient.lname = request.POST.get('lastName')
        patient.gender = 0 if request.POST.get('gender') == 'male' else 1
        patient.save()
        
        pid = patients.objects.filter(HN=request.POST.get('HN_number'))[0].pid
        return HttpResponseRedirect('patientinfo/?pid='+str(pid))
    else : 
        print(request)
        header_str = 'Hello'
        template = loader.get_template('addpatient.html')
        context = {
            'var1': header_str
        }
        return HttpResponse(template.render(context, request))

def patientList(request):
    print(request)
    context = {
        'list_patient': list(patients.objects.all())
    }
    return render(request, 'patient_list.html', context)

def patientInfo(request):
    print(request)
    patient_id = int(request.GET.get('pid'))
    print("pid = " + str(patient_id))
    context = {
        'patient': patients.objects.get(pid = patient_id),
        'patient_info': list(patient_info.objects.filter(pid = patient_id))
    }        
    return render(request, 'patient_info.html', context)
