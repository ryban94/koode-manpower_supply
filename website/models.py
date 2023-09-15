from django.db import models

# Create your models here.
class plogdb(models.Model):
    pfname = models.CharField(max_length=100, null=True, blank=True)
    plname = models.CharField(max_length=500, null=True, blank=True)
    pbirthday = models.CharField(max_length=500, null=True, blank=True)
    pgender = models.CharField(max_length=500, null=True, blank=True)
    pemail = models.CharField(max_length=500, null=True, blank=True)
    pphone = models.IntegerField(null=True, blank=True)
    pqual = models.CharField(max_length=500, null=True, blank=True)
    pskill = models.CharField(max_length=500, null=True, blank=True)
    pcity = models.CharField(max_length=500, null=True, blank=True)
    ppincode= models.IntegerField(null=True, blank=True)
    pid = models.CharField(max_length=500, null=True, blank=True)
    pfile = models.ImageField(upload_to="image", null=True, blank=True)
    ppassword= models.CharField(max_length=500, null=True, blank=True)

class clogdb(models.Model):
    cfname = models.CharField(max_length=100, null=True, blank=True)
    clname = models.CharField(max_length=500, null=True, blank=True)
    cbirthday = models.CharField(max_length=500, null=True, blank=True)
    cgender = models.CharField(max_length=500, null=True, blank=True)
    cemail = models.CharField(max_length=500, null=True, blank=True)
    cphone = models.IntegerField(null=True, blank=True)
    ccity = models.CharField(max_length=500, null=True, blank=True)
    cpincode= models.IntegerField(null=True, blank=True)
    cid = models.CharField(max_length=500, null=True, blank=True)
    cfile = models.ImageField(upload_to="image", null=True, blank=True)
    cpassword= models.CharField(max_length=500, null=True, blank=True)

class postdb(models.Model):
    aphone = models.IntegerField(null=True, blank=True)
    ausername = models.CharField(max_length=100, null=True, blank=True)
    atitle = models.CharField(max_length=100, null=True, blank=True)
    adisc = models.CharField(max_length=1000, null=True, blank=True)
    ars = models.IntegerField(null=True, blank=True)
    aloc = models.CharField(max_length=100, null=True, blank=True)
    acat = models.CharField(max_length=500, null=True, blank=True)
    aphoto = models.ImageField(upload_to="image", null=True, blank=True)
    adate = models.CharField(max_length=100, null=True, blank=True)
    akey = models.CharField(max_length=500, null=True, blank=True)

