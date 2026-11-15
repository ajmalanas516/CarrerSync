from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse 
from django.views.decorators.cache import cache_control
from guestapp.models import tbl_company,tbl_login
from companyapp.models import tbl_internship
from collegeapp.models import tbl_requestiv
from django.http import JsonResponse
from studentapp.models import tbl_requestinternship
from studentapp.models import tbl_student
from adminapp.models import tbl_companytype, tbl_location, tbl_district
from email.message import EmailMessage
import smtplib






# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companyindex(request):
    loginid = request.session.get('loginId')
    if loginid:
        return render(request,'company/index.html')
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def internshipregister(request):
    loginid = request.session.get('loginId')
    if loginid:
        return render(request,'company/internshipregister.html')
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def internshipregister_process(request):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            internshipname = request.POST.get("internshipname")        
            
            iob = tbl_internship()
            iob.internshipname = internshipname
            iob.syllabus = request.FILES['syllabus']
            iob.photo = request.FILES['image']
            iob.amount = request.POST.get("amount")
            iob.duration = request.POST.get("duration")
            iob.description = request.POST.get("description")
            iob.companyid = tbl_company.objects.get(loginid=request.session['loginId'])
            iob.save()
            return HttpResponse("<script>alert('Successfully registered');window.location='internshipregister';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


        


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewinternship(request):
    loginid = request.session.get('loginId')
    if loginid:
        companyid=tbl_company.objects.get(loginid=request.session['loginId'])
        internships = tbl_internship.objects.filter(companyid=companyid)
        return render(request, 'company/internshipdetails.html', {'internships': internships})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteinternship(request,internshipid):
    loginid = request.session.get('loginId')
    if loginid:
        iob = tbl_internship.objects.get(internshipid=internshipid)
        iob.delete()
        return HttpResponse("<script>alert('Successfully Deleted'); window.location='" + reverse('viewinternship') + "';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editinternship(request, internshipid):
    loginid = request.session.get('loginId')
    if loginid:
        iob = tbl_internship.objects.get(internshipid=internshipid)

        if request.method == "POST":
            iob.internshipname = request.POST.get("internshipname")
            iob.amount = request.POST.get("amount")
            iob.duration = request.POST.get("duration")
            iob.description = request.POST.get("description")

            # Update Syllabus File
            if len(request.FILES) != 0 and 'syllabus' in request.FILES:
                iob.syllabus = request.FILES['syllabus']
                
            # Update Image File
            if len(request.FILES) != 0 and 'image' in request.FILES:
                iob.photo = request.FILES['image']

            iob.save()
            return HttpResponse("<script>alert('Successfully Updated'); window.location='" + reverse('viewinternship') + "';</script>")

        else:
            internship = tbl_internship.objects.get(internshipid=internshipid)
            return render(request, 'company/editinternship.html', {'internship': internship})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewvisitrequest(request):
    loginid = request.session.get('loginId')
    if loginid:
        companyid=tbl_company.objects.get(loginid=request.session['loginId'])
        requests = tbl_requestiv.objects.filter(companyid=companyid,status="requested")
        return render(request, 'company/viewvisitrequest.html', {'requests': requests})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def iv_viewmore(request,id):
    loginid = request.session.get('loginId')
    if loginid:
        requests = tbl_requestiv.objects.get(requestid=id)
        return render(request,'company/iv_viewmore.html',{'r':requests})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def AcceptRequest(request, id):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            requests = tbl_requestiv.objects.get(requestid=id)  
            date = request.POST.get("requireddate")
            requests.requireddate = date 
            requests.status = 'Accepted'  
            requests.save()

            # Sending email notification to the college
            college_email = requests.collegeid.collegeemail  # Assuming the college email is stored in tbl_requestiv

            msg = EmailMessage()
            msg.set_content(f"Dear {requests.collegeid.collegename},\n\n"
                            f"Your visit request to {requests.companyid.companyname} has been accepted. "
                            f"The visit is scheduled for {date}. Please be prepared accordingly.\n\n"
                            "Best Regards,\n"
                            f"{requests.companyid.companyname}")

            msg['Subject'] = "Industrial Visit Request Accepted"
            msg['From'] = 'ajmalanas516@gmail.com'  # Replace with your company's email
            msg['To'] = college_email

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login('ajmalanas516@gmail.com', 'sutg zrcm lzmh kveu')  # Use app password if needed
                    smtp.send_message(msg)
            except Exception as e:
                return HttpResponse(f"<script>alert('Email Sending Failed: {str(e)}'); window.location='{reverse('viewvisitrequest')}';</script>")

            return HttpResponse("<script>alert('Successfully Accepted and Email Sent'); window.location='" + reverse('viewvisitrequest') + "';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def RejectRequest(request,id):
    loginid = request.session.get('loginId')
    if loginid:
        requests = tbl_requestiv.objects.get(requestid=id)  
        requests.status = 'Rejected' 
        requests.save() 
        return HttpResponse("<script>alert('Successfully Rejected'); window.location='" + reverse('viewvisitrequest') + "';</script>") 
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

 


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewinternshiprequest(request):
    loginid = request.session.get('loginId')
    if loginid:
        requests = tbl_requestinternship.objects.filter(
        internshipid__companyid__loginid=request.session['loginId'], 
        status="requested"
    )

        return render(request, 'company/viewinternshiprequest.html', {'requests': requests})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def internship_viewmore(request,id):
    loginid = request.session.get('loginId')
    if loginid:
        requests = tbl_requestinternship.objects.get(requestid=id)
        return render(request,'company/internship_viewmore.html',{'r':requests})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_enrolled_students(request):
    loginid = request.session.get('loginId')
    if loginid:
        company = tbl_company.objects.get(loginid=request.session['loginId'])
        enrolled_students = tbl_requestinternship.objects.filter(
            internshipid__companyid=company, status__in=["paid", "completed"]
        ).select_related('studentid', 'internshipid')

        return render(request, 'company/enrolled_students.html', {'enrolled_students': enrolled_students})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def AcceptRequest2(request, id):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            requests = tbl_requestinternship.objects.get(requestid=id) 
            date = request.POST.get("startdate")
            requests.startdate = date   
            requests.status = 'Accepted'  
            requests.save()
            
            # Fetch student details
            student = tbl_student.objects.get(studentid=requests.studentid.studentid)
            internship = tbl_internship.objects.get(internshipid=requests.internshipid.internshipid)
            company = internship.companyid

            # Email details
            recipient_email = student.studentemail
            subject = "Internship Request  Approved"
            body = f"""
            Dear {student.studentname},

            Congratulations! Your request for the internship "{internship.internshipname}" at {company.companyname} has been approved.

            Start Date: {date}
            Company Name:{company.companyname}
            Company Contact: {company.companycontact}

            Please report to the company on the given date.

            Best Regards,  
            {company.companyname}
            """

            # Send Email
            msg = EmailMessage()
            msg.set_content(body)
            msg['Subject'] = subject
            msg['From'] = 'ajmalanas516@gmail.com'  # Use environment variables instead
            msg['To'] = recipient_email

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login('ajmalanas516@gmail.com', 'sutg zrcm lzmh kveu')  # Use environment variables
                    smtp.send_message(msg)
            except Exception as e:
                print("Email sending failed:", e)

            return HttpResponse("<script>alert('Successfully Accepted'); window.location='" + reverse('viewinternshiprequest') + "';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def RejectRequest2(request,id):
    loginid = request.session.get('loginId')
    if loginid:
        requests = tbl_requestinternship.objects.get(requestid=id)  
        requests.status = 'Rejected' 
        requests.save() 
        return HttpResponse("<script>alert('Successfully Rejected'); window.location='" + reverse('viewinternshiprequest') + "';</script>")  
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companyprofile(request):
    loginid = request.session.get('loginId')
    if loginid:
        company = tbl_company.objects.get(loginid=request.session.get('loginId'))
        return render(request, 'company/companyprofile.html', {'company': company})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editcompany(request):
    loginid = request.session.get('loginId')
    if loginid:
        company = tbl_company.objects.get(loginid=request.session.get('loginId'))
        if request.method == "POST":
            company.companyname = request.POST.get("companyname")
            company.companyemail = request.POST.get("companyemail")
            company.companywebsiteurl = request.POST.get("companywebsiteurl")
            if 'companylogo' in request.FILES:
                company.companylogo = request.FILES['companylogo']
            company.companycontact = request.POST.get("companycontact")
            new_username = request.POST.get("username")
            if new_username:
                company.loginid.username = new_username
                company.loginid.save() 

            location_id = request.POST.get("location")
            if location_id:
                company.locationid = tbl_location.objects.get(locationid=location_id)

            company.companytypeid = tbl_companytype.objects.get(companytypeid=request.POST.get("companytype"))
            company.save()
            return HttpResponse("<script>alert('Successfully Updated'); window.location='" + reverse('companyprofile') + "';</script>")
        else:
            district = tbl_district.objects.all()
            companytype = tbl_companytype.objects.all()
            return render(request, 'company/editcompany.html', {'company': company, 'district': district, 'companytype': companytype})  
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
def companychangepassword(request):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == 'POST':
            username = request.POST.get("log_name") 
            password = request.POST.get("log_password")
            newpwd = request.POST.get("newpwd")
            connewpwd = request.POST.get("connewpwd")

            if tbl_login.objects.filter(username=username, password=password).exists():
                lo = tbl_login.objects.get(username=username, password=password)
                if newpwd == connewpwd:
                    lo.password = newpwd  # Update password field
                    lo.save()
                    return HttpResponse(
                        "<script>alert('Successfully updated!!'); window.location='" + reverse("companyindex") + "';</script>")

                else:
                    return HttpResponse(
                        "<script>alert('Password Mismatch !!');window.location='" + reverse("companychangepassword") + "';</script>")
            else:
                return HttpResponse(
                    "<script>alert('Invalid Username or Password!!');window.location='" + reverse("companychangepassword") + "';</script>")

        return render(request, "company/companychangepassword.html")
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

   