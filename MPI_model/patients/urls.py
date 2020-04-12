from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.patientList, name="patient_list"),
    url(r'^addPatient$', views.addpatient, name="add_patient"),
    url(r'^patientInfo$', views.patientInfo, name="patient_info"),
]