from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from patients.models import patients, patient_info

# Create your views here.
def prediction(request):
    print(request)
    no = int(request.GET.get('no'))
    patient_id = patients.objects.filter(patient_info__no = no)[0].pid
    print("No = " + str(no))
    print("pid = " + str(patient_id))
    context = {
        'patient': patients.objects.get(pid = patient_id),
        'patient_info': patient_info.objects.get(no = no)
    }
    return render(request, 'prediction.html', context)

def addPredict(request):
    context = {
        
    }
    return render(request, 'addprediction.html', context)

