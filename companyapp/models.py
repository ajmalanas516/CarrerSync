from django.db import models

# Create your models here.


from adminapp.models import tbl_location
from guestapp.models import tbl_company

class tbl_internship(models.Model):
    internshipid = models.AutoField(primary_key=True)
    internshipname = models.CharField(max_length=100)
    companyid = models.ForeignKey(tbl_company, on_delete=models.CASCADE)
    syllabus = models.FileField()
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    duration = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(default='')

