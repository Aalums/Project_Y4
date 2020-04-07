from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.patientList),
    url(r'^addPatient$', views.addpatient),
    url(r'^patientInfo$', views.patientInfo),
]