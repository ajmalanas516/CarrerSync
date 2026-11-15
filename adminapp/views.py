from email.message import EmailMessage
import json
import smtplib
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse 
from django.utils.timezone import now
from django.views.decorators.cache import cache_control
from django.shortcuts import render,redirect
from adminapp.models import tbl_district
from adminapp.models import tbl_location
from guestapp.models import tbl_login
from adminapp.models import tbl_companytype
from guestapp.models import tbl_company
from guestapp.models import tbl_college
from studentapp.models import tbl_payment
from django.db.models import Count
from companyapp.models import tbl_internship
import xlwt
from django.views.generic import View
from guestapp.models import tbl_student
from collegeapp.models import tbl_requestiv
from django.db.models import Sum
from studentapp.models import tbl_requestinternship
from django.db.models import F

from django.utils.timezone import make_aware, get_current_timezone
from django.views import View
from datetime import datetime
import xlwt
from decimal import Decimal



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminindex(request):
    loginid = request.session.get('loginId')
    if loginid:
        current_year = now().year
        current_month = now().month

        # Get all payments for the current month
        monthly_payments = tbl_payment.objects.filter(
            paymentdate__year=current_year, 
            paymentdate__month=current_month
        )

        # Monthly Earnings
        total_monthly_sales = monthly_payments.aggregate(total_sales=Sum('totalamount'))['total_sales'] or 0
        admin_monthly_earning = monthly_payments.aggregate(admin_total=Sum('adminamount'))['admin_total'] or 0
        company_monthly_earning = monthly_payments.aggregate(company_total=Sum('c_amount'))['company_total'] or 0

        # Entity Counts
        total_confirmed_companies = tbl_company.objects.filter(loginid__status='Confirmed').count()
        total_confirmed_colleges = tbl_college.objects.filter(loginid__status='Confirmed').count()
        total_confirmed_students = tbl_student.objects.filter(loginid__status='Confirmed').count()
        total_internships = tbl_internship.objects.count()
        total_companytypes = tbl_companytype.objects.count()

        # Pie Chart Data: District-wise company distribution
        pie_labels = []
        pie_data = []
        queryset_pie = tbl_company.objects.values('locationid__districtid__districtname').annotate(total_company=Count('companyid'))
        for entry in queryset_pie:
            pie_labels.append(entry['locationid__districtid__districtname'])
            pie_data.append(entry['total_company'])

        # Bar Chart Data: Company-wise confirmed IV requests
        bar_labels = []
        bar_data = []
        queryset_bar = tbl_requestiv.objects.filter(status="confirmed") \
            .values('companyid__companyname') \
            .annotate(total_visit=Count('requestid'))
        for entry in queryset_bar:
            bar_labels.append(entry['companyid__companyname'])
            bar_data.append(entry['total_visit'])

        context = {
            'total_monthly_sales': total_monthly_sales,
            'admin_monthly_earning': admin_monthly_earning,
            'company_monthly_earning': company_monthly_earning,
            'total_confirmed_companies': total_confirmed_companies,
            'total_confirmed_colleges': total_confirmed_colleges,
            'total_confirmed_students': total_confirmed_students,
            'total_internships': total_internships,
            'total_companytypes': total_companytypes,
            'pie_labels_json': json.dumps(pie_labels),
            'pie_data_json': json.dumps(pie_data),
            'bar_labels_json': json.dumps(bar_labels),
            'bar_data_json': json.dumps(bar_data),
        }

        return render(request, 'admin/index.html', context)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def district(request):
    loginid = request.session.get('loginId')
    if loginid:
        return render(request,'admin/district.html')
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def district_process (request):
    loginid = request.session.get('loginId')
    if loginid:

        if request.method == 'POST':
            dname = request.POST.get("districtname")
            dob = tbl_district()
            dob.districtname = dname       
            if tbl_district.objects.filter(districtname=dname).exists():
                
                    return HttpResponse("<script>alert('Already Exists..');window.location='district';</script>")
            else:
                    dob.save()  #insert query
                    return HttpResponse("<script>alert(' Registration succesfully');window.location='district';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

            

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletedistrict(request,districtid):
    loginid = request.session.get('loginId')
    if loginid:

        dob = tbl_district.objects.get(districtid=districtid)
        dob.delete()
        return HttpResponse("<script>alert('Successfully Deleted'); window.location='" + reverse('viewdistrict') + "';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

            

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editdistrict(request, districtid):
    loginid = request.session.get('loginId')
    if loginid:

        if request.method == "POST":
            dob = tbl_district.objects.get(districtid=districtid)
            dob.districtname = request.POST.get('districtname')
            dob.save()
            return HttpResponse("<script> alert ('Updated Successfully');window.location='../viewdistrict';</script>")
        else:
            district = tbl_district.objects.get(districtid=districtid)
            return render(request, 'admin/editdistrict.html', {'district': district})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewdistrict(request):
    loginid = request.session.get('loginId')
    if loginid:
        district = tbl_district.objects.all()
        return render(request,'admin/viewdistrict.html',{'district':district})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def location(request):
    loginid = request.session.get('loginId')
    if loginid:
        district = tbl_district.objects.all()
        return render(request,'admin/location.html',{'district':district})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def location_process (request):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == 'POST':
            districtid=request.POST.get("districtid")
            lname = request.POST.get("locationname")
            lob = tbl_location()
            lob.locationname = lname     
            lob.districtid = tbl_district.objects.get(districtid=districtid)  
            if tbl_location.objects.filter(locationname=lname,districtid=districtid).exists():
                
                    return HttpResponse("<script>alert('Already Exists..');window.location='location';</script>")
            else:
                    lob.save() 
                    return HttpResponse("<script>alert('succesfully Insearted');window.location='location';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewlocation(request):
    loginid = request.session.get('loginId')
    if loginid:
        district = tbl_district.objects.all()
        return render(request,'admin/viewlocation.html',{'district':district})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletelocation(request,locationid):
    loginid = request.session.get('loginId')
    if loginid:
        lob = tbl_location.objects.get(locationid=locationid)
        lob.delete()
        return HttpResponse("<script>alert('Successfully Deleted'); window.location='" + reverse('viewlocation') + "';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editlocation(request, locationid):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            lob = tbl_location.objects.get(locationid=locationid)
            lob.locationname = request.POST.get('locationname')
            lob.save()
            return HttpResponse("<script> alert ('Updated Successfully');window.location='../viewlocation';</script>")
        else:
            location = tbl_location.objects.get(locationid=locationid)
            district = tbl_district.objects.all()
            return render(request, 'admin/editlocation.html', {'location': location,'district':district})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filllocation(request):
    loginid = request.session.get('loginId')
    if loginid:
        districtid = int(request.POST.get("did"))
        location = tbl_location.objects.filter(districtid=districtid).values()
        return JsonResponse(list(location), safe=False)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companytype(request):
    loginid = request.session.get('loginId')
    if loginid:
        return render(request,'admin/companytype.html')
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companytype_process (request):
    loginid = request.session.get('loginId')
    if loginid:

        if request.method == 'POST':
            cname = request.POST.get("companytypename")
            cob = tbl_companytype()
            cob.companytypename = cname       
            if tbl_companytype.objects.filter(companytypename=cname).exists():
                
                    return HttpResponse("<script>alert('Already Exists..');window.location='companytype';</script>")
            else:
                    cob.save()  #insert query
                    return HttpResponse("<script>alert('succesfully Insearted');window.location='companytype';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewcompanytype(request):
    loginid = request.session.get('loginId')
    if loginid:

        companytype = tbl_companytype.objects.all()
        return render(request,'admin/viewcompanytype.html',{'companytype':companytype})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletecompanytype(request, companytypeid):
    loginid = request.session.get('loginId')
    if loginid:
        cob = tbl_companytype.objects.get(companytypeid=companytypeid)
        cob.delete()
        return HttpResponse("<script>alert('Successfully Deleted'); window.location='" + reverse('viewcompanytype') + "';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editcompanytype(request, companytypeid):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            cob = tbl_companytype.objects.get(companytypeid=companytypeid)
            cob.companytypename = request.POST.get('companytypename')
            cob.save()
            return HttpResponse("<script> alert ('Updated Successfully');window.location='../viewcompanytype';</script>")
        else:
            companytype = tbl_companytype.objects.get(companytypeid=companytypeid)
            return render(request, 'admin/editcompanytype.html', {'companytype': companytype})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companyverification(request):
    """ View to display companies pending verification """
    loginid = request.session.get('loginId')
    if loginid:
        company = tbl_company.objects.filter(loginid__status='requested')
        return render(request, "admin/companyverification.html", {'company': company})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def acceptrequest(request, companyid):
    """ Accept company request and send confirmation email """
    loginid = request.session.get('loginId')
    if loginid:
        login = tbl_login.objects.get(loginid=companyid)
        login.status = 'Confirmed'
        login.save()

        # Fetch company details
        company = tbl_company.objects.get(loginid=login)
        send_company_email(company.companyemail, company.companyname, "Confirmed")

        return companyverification(request)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def rejectrequest(request, companyid):
    """ Reject company request and send rejection email """
    loginid = request.session.get('loginId')
    if loginid:
        login = tbl_login.objects.get(loginid=companyid)
        login.status = 'Rejected'
        login.save()

        # Fetch company details
        company = tbl_company.objects.get(loginid=login)
        send_company_email(company.companyemail, company.companyname, "Rejected")

        return companyverification(request)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

def send_company_email(email, company_name, status):
    """ Function to send an email notification to the company upon approval or rejection. """
    subject = "Company Verification Status"
    
    if status == "Confirmed":
        message_content = f"""
        Dear {company_name},

        Congratulations! Your company registration request has been successfully approved. 
        You can now access all CareerSync features.

        Status: Approved

        If you have any questions, feel free to contact us.

        Best regards,  
        CareerSync Team
        """
    else:
        message_content = f"""
        Dear {company_name},

        We regret to inform you that your company registration request has been declined. 
        If you believe this was a mistake, please contact our support team for further clarification.

        Status: Rejected

        Best regards,  
        CareerSync Team
        """

    msg = EmailMessage()
    msg.set_content(message_content)
    msg['Subject'] = subject
    msg['From'] = 'ajmalanas516@gmail.com'
    msg['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('ajmalanas516@gmail.com', 'sutg zrcm lzmh kveu')  # Use environment variables for security
            smtp.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def collegeverification(request):
    loginid = request.session.get('loginId')
    if loginid:
        college = tbl_college.objects.filter(loginid__status='requested')
        return render(request,"admin/collegeverification.html",{'college':college})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def collegeacceptrequest(request, collegeid):
    """ Accept college request and send confirmation email """
    loginid = request.session.get('loginId')
    if loginid:
        login = tbl_login.objects.get(loginid=collegeid)
        login.status = 'Confirmed'
        login.save()

        # Fetch college details
        college = tbl_college.objects.get(loginid=login)
        send_college_email(college.collegeemail, college.collegename, "Confirmed")

        return collegeverification(request)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def collegerejectrequest(request, collegeid):
    """ Reject college request and send rejection email """
    loginid = request.session.get('loginId')
    if loginid:
        login = tbl_login.objects.get(loginid=collegeid)
        login.status = 'Rejected'
        login.save()

        # Fetch college details
        college = tbl_college.objects.get(loginid=login)
        send_college_email(college.collegeemail, college.collegename, "Rejected")

        return collegeverification(request)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

def send_college_email(email, college_name, status):
    """ Function to send an email notification to the college upon approval or rejection. """
    subject = "College Verification Status"
    
    if status == "Confirmed":
        message_content = f"""
        Dear {college_name},

        Congratulations! Your college registration request has been successfully approved. 
        You can now access all CareerSync features.

        Status: Approved

        If you have any questions, feel free to contact us.

        Best regards,  
        CareerSync Team
        """
    else:
        message_content = f"""
        Dear {college_name},

        We regret to inform you that your college registration request has been declined. 
        If you believe this was a mistake, please contact our support team for further clarification.

        Status: Rejected

        Best regards,  
        CareerSync Team
        """

    msg = EmailMessage()
    msg.set_content(message_content)
    msg['Subject'] = subject
    msg['From'] = 'ajmalanas516@gmail.com'
    msg['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('ajmalanas516@gmail.com', 'sutg zrcm lzmh kveu')  # Use environment variables for security
            smtp.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def paymentview(request):
    loginid = request.session.get('loginId')
    if loginid:
        payments = tbl_payment.objects.all()
        
        total_totalamount = sum(payment.totalamount for payment in payments)
        total_adminamount = sum(payment.adminamount for payment in payments)
        total_camount = sum(payment.c_amount for payment in payments)
        
        return render(request, 'admin/paymentview.html', {
            'payment': payments,
            'total_totalamount': total_totalamount,
            'total_adminamount': total_adminamount,
            'total_camount': total_camount
        })
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")






#pie chart companytype based company

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pie_chart_companytype(request):
    loginid = request.session.get('loginId')
    if loginid:
        labels = []
        data = []

        queryset = tbl_company.objects.values('companytypeid__companytypename').annotate(total_company=Count('companyid'))
        
        for s in queryset:
            labels.append(s['companytypeid__companytypename'])
            data.append(s['total_company'])

        return render(request, 'admin/pie_chart_companytype.html', {
            'labels': labels,
            'data': data,
        })
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


#pie chart company based internship

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def piechart_companywiseinternship(request):
    loginid = request.session.get('loginId')
    if loginid:
        labels = []
        data = []

        # Use the correct foreign key reference to access the company name
        queryset = tbl_internship.objects.values('companyid__companyname').annotate(total_internship=Count('internshipid'))
        
        for s in queryset:
            labels.append(s['companyid__companyname'])  # Correct field reference
            data.append(s['total_internship'])

        return render(request, 'admin/piechart_companywiseinternship.html', {
            'labels': labels,
            'data': data,
        })
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



#pie chart district wise company report
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def  piechart_districtwisecompany(request):
    loginid = request.session.get('loginId')
    if loginid:
        labels = []
        data = []

        queryset = tbl_company.objects.values('locationid__districtid__districtname').annotate(total_company=Count('companyid'))

        for s in queryset:
            labels.append(s['locationid__districtid__districtname'])
            data.append(s['total_company'])

        return render(request, 'admin/piechart_districtwisecompany.html', {
            'labels': labels,
            'data': data,
        })
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


#pie chart district wise student report
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def  piechart_districtwisestudent(request):
    loginid = request.session.get('loginId')
    if loginid:
        labels = []
        data = []

        queryset = tbl_student.objects.values('locationid__districtid__districtname').annotate(total_student=Count('studentid'))

        for s in queryset:
            labels.append(s['locationid__districtid__districtname'])
            data.append(s['total_student'])

        return render(request, 'admin/piechart_districtwisestudent.html', {
            'labels': labels,
            'data': data,
        })  
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


     
#pie chart district wise college report
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def  piechart_districtwisecollege(request):
    loginid = request.session.get('loginId')
    if loginid:
        labels = []
        data = []

        queryset = tbl_college.objects.values('locationid__districtid__districtname').annotate(total_college=Count('collegeid'))

        for s in queryset:
            labels.append(s['locationid__districtid__districtname'])
            data.append(s['total_college'])

        return render(request, 'admin/piechart_districtwisecollege.html', {
            'labels': labels,
            'data': data,
        })
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



#pie chart internship request from students

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def piechart_studentinternshipenrolled(request):
    loginid = request.session.get('loginId')
    if loginid:
        labels = []
        data = []

        queryset = tbl_requestinternship.objects.filter(status='paid') \
            .values('internshipid__internshipname') \
            .annotate(total_request=Count('requestid'))

        for s in queryset:
            labels.append(s['internshipid__internshipname'])
            data.append(s['total_request'])

        return render(request, 'admin/piechart_studentinternshipenrolled.html', {
            'labels': labels,
            'data': data,
        })
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



class ExportExcelCollege(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="collegelist.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['College Name', 'Email', 'Contact Number', 'Website URL', 'District', 'Location']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = tbl_college.objects.all().values_list('collegename', 'collegeemail', 'collegecontact','collegewebsiteurl', 'locationid__districtid__districtname','locationid__locationname')
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response
    


class ExportExcelCompany(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="companylist.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Company Name', 'Email', 'Contact Number', 'Website URL','Company Type','District', 'Location']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = tbl_company.objects.all().values_list('companyname', 'companyemail', 'companycontact','companywebsiteurl', 'companytypeid__companytypename','locationid__districtid__districtname','locationid__locationname')
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response


#Bar Chart Company Wise Visit Report

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def barchart_companywisevisit(request):
    loginid = request.session.get('loginId')
    if loginid:
        labels = []
        data = []

        queryset = tbl_requestiv.objects.filter(status="confirmed") \
            .values('companyid__companyname') \
            .annotate(total_visit=Count('requestid'))

        for entry in queryset:
            labels.append(entry['companyid__companyname'])  # Company Name
            data.append(entry['total_visit'])  # Total Visits

        return render(request, 'admin/barchart_companywisevisit.html', {
            'labels': labels,
            'data': data
        })
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    loginid = request.session.get('loginId')
    if loginid:
        request.session.clear()
        return redirect('/')
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



class ExportProfitReport(View):
    def get(self, request):
        return render(request, 'admin/payment_report.html')

    def post(self, request):
        from_date_str = request.POST.get('fromDate')
        to_date_str = request.POST.get('toDate')

        if not from_date_str or not to_date_str:
            return HttpResponse("Both fromDate and toDate are required.")

        from_date = make_aware(datetime.strptime(from_date_str, '%Y-%m-%d'), get_current_timezone())
        to_date = make_aware(datetime.strptime(to_date_str, '%Y-%m-%d'), get_current_timezone())

        payments = tbl_payment.objects.filter(paymentdate__range=(from_date, to_date)) \
            .select_related('requestid__studentid', 'requestid__internshipid', 'requestid__internshipid__companyid') \
            .annotate(
                student_name=F('requestid__studentid__studentname'),
                company_name=F('requestid__internshipid__companyid__companyname'),
                internship_name=F('requestid__internshipid__internshipname')
            ) \
            .values(
                'requestid',
                'student_name',
                'company_name',
                'internship_name',
                'totalamount',
                'paymentdate'
            )

        total_amount = payments.aggregate(Sum('totalamount'))['totalamount__sum'] or 0.0

        if 'export_excel' in request.POST:
            return self.export_to_excel(payments, from_date_str, to_date_str, total_amount)

        context = {
            'from_date': from_date_str,
            'to_date': to_date_str,
            'report_data': payments,
            'total_amount': total_amount
        }

        return render(request, 'admin/payment_report.html', context)

 

    def export_to_excel(self, payments, from_date, to_date, total_amount):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="payment_report_{from_date}_to_{to_date}.xls"'

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Payments')

        # Define the columns
        columns = ['SI NO', 'Student Name', 'Company Name', 'Internship Name', 'Total Amount', 'Payment Date']
        
        # Apply header style
        header_style = xlwt.easyxf("font: bold on; align: horiz center")

        # Write column headers
        for col_num, column_title in enumerate(columns):
            ws.write(0, col_num, column_title, header_style)

        # Write data rows
        for row_num, row_data in enumerate(payments, start=1):
            ws.write(row_num, 0, row_num)  # Serial Number
            ws.write(row_num, 1, row_data['student_name'])
            ws.write(row_num, 2, row_data['company_name'])
            ws.write(row_num, 3, row_data['internship_name'])
            ws.write(row_num, 4, f"₹{row_data['totalamount']:.2f}")
            ws.write(row_num, 5, row_data['paymentdate'].strftime('%Y-%m-%d'))

        # Write total amount at the bottom
        total_row = len(payments) + 1
        ws.write(total_row, 3, "Total Amount:", xlwt.easyxf("font: bold on"))
        ws.write(total_row, 4, f"₹{total_amount:.2f}", xlwt.easyxf("font: bold on"))

        wb.save(response)
        return response

    



def StudentReportView(request):
    students = tbl_student.objects.select_related('locationid').all()
    return render(request, 'Admin/student_report.html', {'students': students})


class ExportStudentReport(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="student_report.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Student Report')

        # Define column headings
        row_num = 0
        columns = [
            'Student Name', 'Email', 'Contact', 'Date of Birth', 'Location',
            'College Name', 'Course', 'Semester'
        ]

        # Add column headers with bold formatting
        bold_style = xlwt.easyxf('font: bold 1')
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title, bold_style)
            ws.col(col_num).width = 5000  # Adjust column width for readability

        # Query student data
        students = tbl_student.objects.select_related('locationid').all()

        # Write student data to the worksheet
        for student in students:
            row_num += 1
            ws.write(row_num, 0, student.studentname)  # Student Name
            ws.write(row_num, 1, student.studentemail)  # Email
            ws.write(row_num, 2, student.studentcontact)  # Contact
            ws.write(row_num, 3, student.studentdateofbirth.strftime('%d-%m-%Y'))  # Date of Birth
            ws.write(row_num, 4, student.locationid.locationname)  # Location
            ws.write(row_num, 5, student.collegename)  # College Name
            ws.write(row_num, 6, student.course)  # Course
            ws.write(row_num, 7, student.sem)  # Semester

        wb.save(response)
        return response
