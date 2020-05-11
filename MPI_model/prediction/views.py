from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from patients.models import patients, patient_info
import pickle

def prediction(request):
    if request.method == 'POST':
        print(request)
        no = int(request.GET.get('no'))
        patient_id = patients.objects.filter(patient_info__no = no)[0].pid
        method = request.POST.get('_method')
        print(method)
        if method == 'Save' :
            CAG_confirm = request.POST.get('CAG_confirm')
            if CAG_confirm != patient_info.objects.get(no = no).CAG_confirm :
                print("Update CAG_confirm of No : " + str(no))
                print("Old : " + str(patient_info.objects.get(no = no).CAG_confirm) + " New : " + str(CAG_confirm))
                patient_info.objects.filter(no = no).update(CAG_confirm = CAG_confirm)
            context = {
            'patient': patients.objects.get(pid = patient_id),
            'patient_info': patient_info.objects.get(no = no)
            }
            return render(request, 'prediction.html', context)
        else :
            print("Delete No : " + str(no))
            patient_info.objects.filter(no = no).delete()
            context = {
                'patient': patients.objects.get(pid = patient_id),
                'patient_info': list(patient_info.objects.filter(pid = patient_id))
            }
            return render(request, 'patient_info.html', context)

    else :
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
    print(request)
    patient_id =  int(request.GET.get('pid'))
    print("pid = " + str(patient_id))
    context = {
        'patient': patients.objects.get(pid = patient_id)
    }
    return render(request, 'addprediction.html', context)

def predict(request):
    data = []
    p_info = patient_info()

    if(request.method == 'POST'):
        pid = request.POST.get('pid')
        
        #patients characteristic
        date = request.POST.get('date')
        print(date)
        age = int(request.POST.get('age'))
        bmi = int(request.POST.get('bmi'))
        dm = 0 if request.POST.get('dm') == 'Negative' else 1
        ht = 0 if request.POST.get('ht') == 'Negative' else 1
        dlp = 0 if request.POST.get('dlp') == 'Negative' else 1
        ckd = 0 if request.POST.get('ckd') == 'Negative' else 1

        #MPI feature 
        #LAD
        lad_4dmspect = float(request.POST.get('lad_4dmspect'))
        lad_wallthick = float(request.POST.get('lad_wallthick'))
        lad_wallmotion = float(request.POST.get('lad_wallmotion'))

        #LCX
        lcx_4dmspect = float(request.POST.get('lcx_4dmspect'))
        lcx_wallthick = float(request.POST.get('lcx_wallthick'))
        lcx_wallmotion = float(request.POST.get('lcx_wallmotion'))
        
        #RCA
        rca_4dmspect = float(request.POST.get('rca_4dmspect'))
        rca_wallthick = float(request.POST.get('rca_wallthick'))
        rca_wallmotion = float(request.POST.get('rca_wallmotion'))
        
        lvef = int(request.POST.get('lvef'))
        #model
        model = pickle.load(open("static/model/model_mpi", "rb"))
        print(model)
    return render(request, 'predict.html')

