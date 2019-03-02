from django.db import models
from django.urls import reverse

# Create your models here.

class CBCresults(models.Model):
    date = models.DateField(auto_now=False)
    HCT_percent = models.DecimalField(max_digits=4, decimal_places=2)
    Hgb = models.DecimalField(max_digits=4, decimal_places=2)
    MCV = models.DecimalField(max_digits=4, decimal_places=2)
    NRBC = models.DecimalField(max_digits=5, decimal_places=2)
    Platelets = models.IntegerField()
    RBCs = models.DecimalField(max_digits=4, decimal_places=2)
    RDW_RBC_percent = models.DecimalField(max_digits=4, decimal_places=2)
    WBC = models.DecimalField(max_digits=4, decimal_places=2)

    def get_absolute_url(self ):
        return reverse('cbcresultslist')

class WBCdifferential(models.Model):
    date = models.DateField(auto_now=False)
    LYMPHS_MAN_CNT = models.IntegerField()
    MONOS_MAN_CNT = models.DecimalField(max_digits=2, decimal_places=2)
    NEUTROPHILS_MAN_CNT = models.DecimalField(max_digits=2, decimal_places=2)
    PLTS_MORPH = models.DecimalField(max_digits=2, decimal_places=2)
    PLTs_BLD_QL_MAN = models.DecimalField(max_digits=2, decimal_places=2)
    NEUTROPHILS_CALCULATED = models.DecimalField(max_digits=2, decimal_places=2)
 
    def get_absolute_url(self):
        return reverse('cbcresultslist')