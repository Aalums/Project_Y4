from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from patients.models import patients, patient_info

# Create your views here.
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
        patient_id =  int(request.GET.get('pid'))
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

