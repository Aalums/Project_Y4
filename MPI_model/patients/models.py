from django.db import models

# Create your models here.
class patients(models.Model):
    pid = models.AutoField(primary_key=True)
    HN = models.CharField(max_length=9)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    gender = models.IntegerField()

class patient_info(models.Model):
    no = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    age = models.IntegerField()
    BMI = models.DecimalField(max_digits=20, decimal_places=2)
    DM = models.IntegerField()
    HT = models.IntegerField()
    DLP = models.IntegerField()
    CKD = models.IntegerField()
    # LAD
    LAD4dmspect = models.DecimalField(max_digits=20, decimal_places=2)
    LADwallthick = models.DecimalField(max_digits=20, decimal_places=2)
    LADwallmotion = models.DecimalField(max_digits=20, decimal_places=2)
    LADCAG = models.IntegerField()
    # LCX
    LCX4dmspect = models.DecimalField(max_digits=20, decimal_places=2)
    LCXwallthick = models.DecimalField(max_digits=20, decimal_places=2)
    LCXwallmotion = models.DecimalField(max_digits=20, decimal_places=2)
    LCXCAG = models.IntegerField()
    # RCA
    RCA4dmspect = models.DecimalField(max_digits=20, decimal_places=2)
    RCAwallthick = models.DecimalField(max_digits=20, decimal_places=2)
    RCAwallmotion = models.DecimalField(max_digits=20, decimal_places=2)
    RCACAG = models.IntegerField()
    LVEF = models.IntegerField()
    pid = models.ForeignKey(patients, on_delete=models.CASCADE)
