from django.db import models


# Create your models here.
class tbl_login(models.Model):
    loginid= models.AutoField(primary_key=True)
    username= models.CharField(max_length=25)
    password= models.CharField(max_length=25)
    role= models.CharField(max_length=25)
    status= models.CharField(max_length=25)

from adminapp.models import tbl_location,tbl_companytype
class tbl_company(models.Model):
    companyid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=100)
    companylogo = models.ImageField()
    locationid= models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    companyemail = models.CharField(max_length=100, unique=True)
    companycontact = models.BigIntegerField()
    companywebsiteurl = models.CharField(max_length=200)
    companytypeid = models.ForeignKey(tbl_companytype, on_delete=models.CASCADE)
    loginid = models.ForeignKey(tbl_login, on_delete=models.CASCADE)      

class tbl_college(models.Model):
    collegeid = models.AutoField(primary_key=True)
    collegename = models.CharField(max_length=100)
    collegephoto = models.ImageField(default='')
    locationid= models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    collegeemail = models.CharField(max_length=100, unique=True)
    collegecontact = models.BigIntegerField()
    collegewebsiteurl = models.CharField(max_length=200)
    loginid = models.ForeignKey(tbl_login, on_delete=models.CASCADE)      


class tbl_student(models.Model):
    studentid = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=100)
    studentphoto = models.ImageField(default='')
    studentemail = models.CharField(max_length=100, unique=True)
    studentcontact = models.BigIntegerField()
    studentdateofbirth = models.DateField()
    locationid= models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    collegename = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    sem = models.BigIntegerField()
    loginid = models.ForeignKey(tbl_login, on_delete=models.CASCADE)     