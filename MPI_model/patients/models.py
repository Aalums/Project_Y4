from django.db import models

# Create your models here.
class patients(models.Model):
    HN = models.CharField(max_length=9)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

class patient_characteristic(models.Model):
    cha_id = models.AutoField(primary_key=True)
    cha_date = models.DateTimeField(auto_now_add=True, blank=True)
    bmi = models.DecimalField(max_digits=20, decimal_places=2)
    dm = models.CharField(max_length=1)
    ht = models.CharField(max_length=1)
    dlp = models.CharField(max_length=1)
    ckd = models.CharField(max_length=1)
    HN = models.ForeignKey(patients, on_delete=models.CASCADE)

class patient_mpi(models.Model):
    mpi_id = models.AutoField(primary_key=True)
    mpi_date = models.DateTimeField(auto_now_add=True, blank=True)
    # LAD
    LAD_4dmspect = models.DecimalField(max_digits=20, decimal_places=2)
    LAD_wallthick = models.DecimalField(max_digits=20, decimal_places=2)
    LAD_wallmotion = models.DecimalField(max_digits=20, decimal_places=2)
    LAD_CAG = models.CharField(max_length=1)
    # LCX
    LCX_4dmspect = models.DecimalField(max_digits=20, decimal_places=2)
    LCX_wallthick = models.DecimalField(max_digits=20, decimal_places=2)
    LCX_wallmotion = models.DecimalField(max_digits=20, decimal_places=2)
    LCX_CAG = models.CharField(max_length=1)
    # RCA
    RCA_4dmspect = models.DecimalField(max_digits=20, decimal_places=2)
    RCA_wallthick = models.DecimalField(max_digits=20, decimal_places=2)
    RCA_wallmotion = models.DecimalField(max_digits=20, decimal_places=2)
    RCA_CAG = models.CharField(max_length=1)
    LVEF = models.IntegerField()
    HN = models.ForeignKey(patients, on_delete=models.CASCADE)
    # cha_id = models.ForeignKey(patients, on_delete=models.CASCADE)