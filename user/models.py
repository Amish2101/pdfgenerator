from django.db import models

class user(models.Model):
    user = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user


class reports(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.report_name


class pathology(models.Model):
    pathology = models.TextField(max_length=100000, blank=True)
    report_name = models.ForeignKey(reports,  on_delete=models.CASCADE)

    def __str__(self):
        return self.pathology

class cbcreport(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    report_name = models.ForeignKey(reports, on_delete=models.ForeignKey)
    hb = models.FloatField(blank=True)
    rbc = models.FloatField(blank=True)
    wbc = models.FloatField(blank=True)
    platelet = models.FloatField(blank=True)
    hematocrit = models.FloatField(blank=True)
    mcv = models.FloatField(blank=True)
    mch = models.FloatField(blank=True)
    mchc = models.FloatField(blank=True)
    neutrophils = models.FloatField(blank=True)
    lymphocytes = models.FloatField(blank=True)
    eosinophils = models.FloatField(blank=True)
    monocytes = models.FloatField(blank=True)
    basophils = models.FloatField(blank=True)
    paots = models.CharField(max_length=100,blank=True)
    pfm = models.CharField(max_length=100,blank=True)
    microcytosis = models.CharField(max_length=100,blank=True)
    hyphochromia = models.CharField(max_length=100,blank=True)
    anisocytosis = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.user
    



