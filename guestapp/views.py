import random
import string
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from guestapp.models import tbl_login
from adminapp.models import tbl_district
from guestapp.models import tbl_company
from adminapp.models import tbl_location
from adminapp.models import tbl_companytype
from guestapp.models import tbl_college
from guestapp.models import tbl_student
from email.message import EmailMessage
import smtplib

from studentapp.models import tbl_requestinternship




# Create your views here.


def guestindex(request):
    return render(request,'guest/index.html')

def login(request):
    return render(request,'guest/login.html')

from django.shortcuts import render, redirect
from .models import tbl_login




def login_process(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if tbl_login.objects.filter(username=username, password=password).exists():
            logindata = tbl_login.objects.get(username=username, password=password)
            request.session['loginId'] = logindata.loginid
            role = logindata.role

            if role == "admin":
                return redirect('adminapp/adminindex')

            elif role == "company":
                if logindata.status == "Confirmed":
                    return redirect('companyapp/companyindex')
                else:
                    return render(request, "guest/login.html", {"error": "Please wait for confirmation."})

            elif role == "college":
                if logindata.status == "Confirmed":
                    return redirect('collegeapp/collegeindex')
                else:
                    return render(request, "guest/login.html", {"error": "Please wait for confirmation."})

            elif role == "student":
                return redirect('studentapp/studentindex')

        else:
            return render(request, "guest/login.html", {"error": "Incorrect username or password"})

    return render(request, "guest/login.html")  # Ensure proper handling for GET requests





def companyregister(request):
    district = tbl_district.objects.all()
    companytype = tbl_companytype.objects.all()
    return render(request, 'guest/companyregister.html',{'district': district,'companytype':companytype})

def companyregister_process(request):
    if request.method == "POST":
        lob = tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role="company"
        lob.status="requested"
        if tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..');window.location='companyregister';</script>")
        else:
            lob.save()
            dob = tbl_company()
            dob.companyname = request.POST.get("companyname")
            dob.companylogo = request.FILES["companylogo"]
            dob.companyemail = request.POST.get("companyemail")
            dob.companycontact = request.POST.get("companycontactnumber")
            dob.companywebsiteurl = request.POST.get("companywebsiteurl")
            dob.loginid = lob
            dob.locationid = tbl_location.objects.get(locationid=request.POST.get("location"))
            dob.companytypeid = tbl_companytype.objects.get(companytypeid=request.POST.get("companytype"))
            dob.save()
            Email=request.POST.get('companyemail')  # to address
            msg = EmailMessage()
            msg.set_content(f"""
            Dear {request.POST.get("companyname")},  
            Thank you for registering with CareerSync. Your registration request has been successfully received and is currently under review.  
            Here are your login details:  
            Username:{request.POST.get("username")}  
            Password:{request.POST.get("password")}
            Email: {request.POST.get("companyemail")}  
            Status: Pending Approval  
            We will notify you once your registration is approved. If you have any questions, feel free to contact us.  

            Best regards,  
            CareerSync Team  
            """)

            msg['Subject'] = "Registration Completed"
            msg['from'] = 'ajmalanas516@gmail.com'
            msg['To'] = {Email}
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('ajmalanas516@gmail.com','sutg zrcm lzmh kveu')
                smtp.send_message(msg)
            return HttpResponse("<script>alert('Successfully registered');window.location='companyregister';</script>")
        
def collegeregister(request):
    district = tbl_district.objects.all()
    return render(request, 'guest/collegeregister.html',{'district': district})

def collegeregister_process(request):
    if request.method == "POST":
        lob = tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role="college"
        lob.status="requested"
        if tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..');window.location='collegeregister';</script>")
        else:
            lob.save()
            dob = tbl_college()
            dob.collegename = request.POST.get("collegename")
            dob.collegephoto = request.FILES["collegephoto"]
            dob.collegeemail = request.POST.get("collegeemail")
            dob.collegecontact = request.POST.get("collegecontactnumber")
            dob.collegewebsiteurl = request.POST.get("collegewebsiteurl")
            dob.loginid = lob
            dob.locationid = tbl_location.objects.get(locationid=request.POST.get("location"))
            dob.save()
            Email=request.POST.get('collegeemail')  # to address
            msg = EmailMessage()
            msg.set_content(f"""
            Dear {request.POST.get("collegename")},  
            Thank you for registering with CareerSync. Your registration request has been successfully received and is currently under review.  
            Here are your login details:  
            Username:{request.POST.get("username")}  
            Email: {request.POST.get("collegeemail")}  
            Status: Pending Approval  
            We will notify you once your registration is approved. If you have any questions, feel free to contact us.  

            Best regards,  
            CareerSync Team  
            """)
            msg['Subject'] = "Registration Completed"
            msg['from'] = 'ajmalanas516@gmail.com'
            msg['To'] = {Email}
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('ajmalanas516@gmail.com','sutg zrcm lzmh kveu')
                smtp.send_message(msg)


            return HttpResponse("<script>alert('Successfully registered');window.location='collegeregister';</script>")
        
def studentregister(request):
    district = tbl_district.objects.all()
    return render(request, 'guest/studentregister.html',{'district': district})

def studentregister_process(request):
    if request.method == "POST":
        lob = tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role="student"
        lob.status="confirmed"
        if tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..');window.location='studentregister';</script>")
        else:
            lob.save()
            dob = tbl_student()
            dob.studentname = request.POST.get("studentname")
            dob.studentphoto = request.FILES['studentphoto']
            dob.studentemail = request.POST.get("studentemail")
            dob.studentcontact = request.POST.get("studentcontactnumber")
            dob.studentdateofbirth = request.POST.get("studentdateofbirth")
            dob.collegename = request.POST.get("collegename")
            dob.course = request.POST.get("course")
            dob.sem = request.POST.get("semester")
            dob.loginid = lob
            dob.locationid = tbl_location.objects.get(locationid=request.POST.get("location"))
            dob.save()
            Email=request.POST.get('studentemail')  # to address
            msg = EmailMessage()
            msg.set_content(f"""
            Dear {request.POST.get("studentname")},  
            Thank you for registering with CareerSync. Your registration request has been successfully received and is currently under review.  
            Here are your login details:  
            Username:{request.POST.get("username")}  
            Email: {request.POST.get("studentemail")} 
            Password: {request.POST.get("password")} 
            Status:  Approved 
            If you have any questions, feel free to contact us.  

            
            Best regards,  
            CareerSync Team  
            """)            
            msg['Subject'] = "Registration Completed"
            msg['from'] = 'ajmalanas516@gmail.com'
            msg['To'] = {Email}
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('ajmalanas516@gmail.com','sutg zrcm lzmh kveu')
                smtp.send_message(msg)



            return HttpResponse("<script>alert('Successfully registered');window.location='studentregister';</script>")
        
# def filllocation(request):
#      districtid = int(request.POST.get("did"))
#      location = tbl_location.objects.filter(districtid=districtid).values()
#      return JsonResponse(list(location), safe=False)



def filllocationnew(request):
    did = int(request.POST.get("did"))
    location = tbl_location.objects.filter(districtid=did).values()
    return JsonResponse(list(location), safe=False)


def guestindex(request):
    update_completed(request)
    return render(request,'guest/index.html')



from datetime import datetime
import re
from dateutil.relativedelta import relativedelta



def update_completed(request):
    today = datetime.today().date()
    
    requests = tbl_requestinternship.objects.filter(status="paid").select_related('internshipid')

    for req in requests:
        if req.startdate:
            # Extract number of months from the 'duration' field
            match = re.search(r'(\d+)', req.internshipid.duration)
            if match:
                months = int(match.group(1))
                end_date = req.startdate + relativedelta(months=months)

                if end_date < today:
                    req.status = "completed"
                    req.save()
    
    return JsonResponse({"message": "Update completed successfully"})

            
        
def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get("username")

        # ✅ Check if user exists
        if tbl_login.objects.filter(username=username).exists():
            user = tbl_login.objects.get(username=username)

            # ✅ Find user type (Adopter or Provider)
            email = None
            name = None
            user_type = None

            if tbl_company.objects.filter(loginid_id=user.loginid).exists():
                company = tbl_company.objects.get(loginid_id=user.loginid)
                email = company.companyemail
                name = company.companyname
                user_type = "company"

            elif tbl_college.objects.filter(loginid_id=user.loginid).exists():
                college = tbl_college.objects.get(loginid_id=user.loginid)
                email = college.collegeemail
                name = college.collegename
                user_type = "college"
            
            elif tbl_student.objects.filter(loginid_id=user.loginid).exists():
                student = tbl_student.objects.get(loginid_id=user.loginid)
                email = student.studentemail
                name = student.studentname
                user_type = "student"
            

            else:
                return HttpResponse("<script>alert('No email found for this user.');window.location='/guestapp/forgot_password';</script>")

            # ✅ Generate a new random password
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

            # ✅ Update password in the database
            user.password = new_password  # Hash this for security
            user.save()

            # ✅ Send email
            msg = EmailMessage()
            msg.set_content(
                f"Hello {name},\n\n"
                f"We received a request to reset your password. Your new password is:\n\n"
                f"🔑 {new_password}\n\n"
                "For security reasons, please log in and change your password immediately.\n\n"
                "Best Regards,\n"
                "Career Sync"
            )
            msg['Subject'] = f"Password Reset Request - Career Sync ({user_type})"
            msg['From'] = "ajmalanas516@gmail.com"
            msg['To'] = email

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login("ajmalanas516@gmail.com", 'sutg zrcm lzmh kveu')  # ✅ Use App Password
                    smtp.send_message(msg)
            except Exception as e:
                return HttpResponse(f"<script>alert('Error sending email: {str(e)}');window.location='/forgot_password';</script>")

            return HttpResponse("<script>alert('New password sent to your email.');window.location='/login';</script>")

        else:
            return HttpResponse("<script>alert('Username not found.');window.location='/forgot_password';</script>")

    return render(request, "guest/forgot_password.html")

    