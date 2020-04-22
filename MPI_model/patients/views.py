from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import patients, patient_info

# Create your views here.
def addpatient(request):
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
    if request.method == 'POST':
        patient = patients()
        patient.HN = request.POST.get('HN_number')
        # patient.date = request.POST.get('date')
        patient.fname = request.POST.get('firstName')
        patient.lname = request.POST.get('lastName')
        # patient.age = request.POST.get('age')
        patient.gender = 0 if request.POST.get('gender') == 'male' else 1
        patient.save()

        pid_1 = patients.objects.filter(request.POST.get('HN_number')).pid
        patientInfo(Request(method='GET', pid=pid_1))

    else :
        patient_id = int(request.GET.get('pid'))
        print("pid = " + str(patient_id))
        context = {
            'patient': patients.objects.filter(pid = patient_id).first(),
            'patient_info': list(patient_info.objects.filter(pid = patient_id))
        }
        return render(request, 'patient_info.html', context)
