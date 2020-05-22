from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from patients.models import patients, patient_info
import pickle
import pandas as pd

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
    if request.method == 'POST':
        print(request)
        patient_id =  int(request.POST.get('pid'))
        print("Add Info pid = " + str(patient_id))
        patientInfo = patient_info()
        patientInfo.age = request.POST.get('age')
        patientInfo.BMI = request.POST.get('bmi')
        patientInfo.DM = request.POST.get('dm')
        patientInfo.HT = request.POST.get('ht')
        patientInfo.DLP = request.POST.get('dlp')
        patientInfo.CKD = request.POST.get('ckd')
        patientInfo.LAD4dmspect = request.POST.get('lad_4dmspect')
        patientInfo.LADwallthick = request.POST.get('lad_wallthick')
        patientInfo.LADwallmotion = request.POST.get('lad_wallmotion')
        patientInfo.LCX4dmspect = request.POST.get('lcx_4dmspect')
        patientInfo.LCXwallthick = request.POST.get('lcx_wallthick')
        patientInfo.LCXwallmotion = request.POST.get('lcx_wallmotion')
        patientInfo.RCA4dmspect = request.POST.get('rca_4dmspect')
        patientInfo.RCAwallthick = request.POST.get('rca_wallthick')
        patientInfo.RCAwallmotion = request.POST.get('rca_wallmotion')
        patientInfo.LVEF = request.POST.get('lvef')
        patientInfo.pid = patients.objects.get(pid = patient_id)
        patientInfo.save()
        
        no = int(patient_info.objects.latest('no').no)
        return HttpResponseRedirect('/prediction?no='+str(no))
    else :
        print(request)
        patient_id =  int(request.GET.get('pid'))
        print("pid = " + str(patient_id))
        context = {
            'patient': patients.objects.get(pid = patient_id)
        }
        return render(request, 'addprediction.html', context)

def predict(request):
    if(request.method == 'POST'):
        pid = request.POST.get('pid')
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
        data = {'LAD4dmspect': [lad_4dmspect], 'LADWallthick': [lad_wallthick], 'LADWallmotion':[lad_wallmotion], 'LCX4dmspect': [lcx_4dmspect], 'LCXWallthick': [lcx_wallthick] , 'LCXWallmotion': [lcx_wallmotion], 'RCA4dmspect': [rca_4dmspect], 'RCAWallthick': [rca_wallthick], 'RCAWallmotion': [rca_wallmotion], 'LVEF': [lvef]}
        file_d = open("static/model/model_mpi", "rb")
        model = pickle.load(file_d)
        df = pd.DataFrame(data)
        print(df)
        print(model)
        result = model.predict(df.as_matrix())
        file_d.close
        addPredict(request)
        no = int(patient_info.objects.latest('no').no)
    return HttpResponseRedirect('/prediction?no='+str(no))

