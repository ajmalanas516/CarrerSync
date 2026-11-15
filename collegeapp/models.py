from django.db import models

# Create your models here.


from guestapp.models import tbl_college
from guestapp.models import tbl_company

class tbl_requestiv(models.Model):
    requestid = models.AutoField(primary_key=True)
    requestdate = models.DateField(auto_now_add=True)
    requireddate = models.DateField(null=True)
    noofstudents = models.BigIntegerField() 
    studentdetails = models.FileField()
    collegeid = models.ForeignKey(tbl_college, on_delete=models.CASCADE)
    status= models.CharField(max_length=25)
    companyid = models.ForeignKey(tbl_company, on_delete=models.CASCADE,default='')


