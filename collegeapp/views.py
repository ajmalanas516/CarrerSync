from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from django.urls import reverse 
from django.http import JsonResponse
from adminapp.models import tbl_district
from adminapp.models import tbl_location
from adminapp.models import tbl_companytype
from guestapp.models import tbl_company
from collegeapp.models import tbl_requestiv
from guestapp.models import tbl_college,tbl_login
import smtplib
from email.message import EmailMessage
from django.http import HttpResponse


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def collegeindex(request):
    loginid = request.session.get('loginId')
    if loginid:
        return render(request,'college/index.html')
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")





def search(request):
    loginid = request.session.get('loginId')
    if loginid:
        district = tbl_district.objects.all()
        companytype = tbl_companytype.objects.all()
        return render(request, 'college/search.html', {'district': district, 'companytype': companytype})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



def filllocationandcompany1(request):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            districtid = int(request.POST.get("did"))

            # Fetch locations in the selected district
            locations = tbl_location.objects.filter(districtid=districtid).values("locationid", "locationname")

            # Fetch only companies with confirmed status
            companies = (
                tbl_company.objects.filter(locationid__districtid=districtid, loginid__status="Confirmed")
                .values("companyid", "companyname", "companylogo")
            )

            response_data = {
                "locations": list(locations),
                "companies": list(companies),
            }

            return JsonResponse(response_data, safe=False)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



def fillcompanytypeandcompany1(request):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            locationid = int(request.POST.get("lid"))

            # Fetch company types of confirmed companies in the selected location
            company_types = (
                tbl_company.objects.filter(locationid=locationid, loginid__status="Confirmed")
                .values("companytypeid_id", "companytypeid__companytypename")
                .distinct()
            )
            company_type_list = [
                {"companytypeid": c["companytypeid_id"], "companytypename": c["companytypeid__companytypename"]}
                for c in company_types
            ]

            # Fetch only confirmed companies in the selected location
            companies = (
                tbl_company.objects.filter(locationid=locationid, loginid__status="Confirmed")
                .values("companyid", "companyname", "companylogo")
            )

            response_data = {
                "companytypes": company_type_list,
                "companies": list(companies),
            }

            return JsonResponse(response_data, safe=False)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")




def fillcompany1(request):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
            locationid = request.POST.get("lid")
            companytypeid = request.POST.get("ctid")

            # Fetch only confirmed companies based on location and company type
            companies = tbl_company.objects.filter(
                locationid=locationid, 
                companytypeid=companytypeid, 
                loginid__status="Confirmed"
            ).values("companyid", "companyname", "companylogo")

            company_list = [
                {"companyid": c["companyid"], "companyname": c["companyname"], "companylogo": c["companylogo"]}
                for c in companies
            ]

            return JsonResponse(company_list, safe=False)
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")





        

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestiv(request,companyid):
    loginid = request.session.get('loginId')
    if loginid:
        return render(request,'college/requestiv.html', {'companyid': companyid})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestiv_process(request):
    loginid = request.session.get('loginId')
    if loginid:
        if request.method == "POST":
                iob = tbl_requestiv()
                college = tbl_college.objects.get(loginid=request.session.get('loginId'))
                iob.companyid = tbl_company.objects.get(companyid=request.POST.get("companyid"))
                iob.collegeid = college
                iob.noofstudents = request.POST.get("noofstudents")
                iob.studentdetails = request.FILES['studentdetails']
                iob.status = "requested"
                iob.save()
                return HttpResponse("<script>alert('Successfully submitted IV request!');window.location='" + reverse('search') + "';</script>")
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

        


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def ivrequeststatus(request):
    loginid = request.session.get('loginId')
    if loginid:
        collegeid=tbl_college.objects.get(loginid=request.session['loginId'])
        requests = tbl_requestiv.objects.filter(collegeid=collegeid)
        return render(request, 'college/ivrequeststatus.html', {'requests': requests})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

        

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def collegeprofile(request):
    loginid = request.session.get('loginId')
    if loginid:
        college = tbl_college.objects.get(loginid=request.session.get('loginId'))
        return render(request, 'college/collegeprofile.html', {'college': college})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editcollegeprofile(request):
    loginid = request.session.get('loginId')
    if loginid:
        college = tbl_college.objects.get(loginid=request.session.get('loginId'))
        if request.method == "POST":
            college.collegename = request.POST.get("collegename")
            college.collegeemail = request.POST.get("collegeemail")
            college.collegewebsiteurl = request.POST.get("collegewebsiteurl")
            if 'collegephoto' in request.FILES:
                college.collegephoto = request.FILES['collegephoto']
            college.collegecontact = request.POST.get("collegecontact")
            new_username = request.POST.get("username")
            if new_username:
                college.loginid.username = new_username
                college.loginid.save() 
            location_id = request.POST.get("location")
            if location_id:
                college.locationid = tbl_location.objects.get(locationid=location_id)

            college.save()
            return HttpResponse("<script>alert('Successfully Updated'); window.location='" + reverse('collegeprofile') + "';</script>")
        else:
            district = tbl_district.objects.all()
            return render(request, 'college/editcollegeprofile.html', {'college': college, 'district': district})
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")

        
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def filllocation(request):
#     loginid = request.session.get('loginId')
#     if loginid:
#         districtid = int(request.POST.get("did"))
#         location = tbl_location.objects.filter(districtid=districtid).values()
#         return JsonResponse(list(location), safe=False)
#     else:
#         return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cancel(request, id):
        loginid = request.session.get('loginId')
        if loginid:
            req = tbl_requestiv.objects.get(requestid=id)
            req.status = 'cancelled'
            req.save() 
            return HttpResponse("<script>alert('Successfully Cancelled'); window.location='" + reverse('ivrequeststatus') + "';</script>")
        else:
            return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def confirm(request, id):
    loginid = request.session.get('loginId')
    if loginid:
        req = tbl_requestiv.objects.get(requestid=id)
        req.status = 'confirmed'
        req.save()

        # Fetch company and college details
        company = req.companyid
        college = req.collegeid

        # Ensure the company has an email field
        if not hasattr(company, 'companyemail') or not company.companyemail:
            return HttpResponse("<script>alert('Company email not found. Cannot send confirmation.'); window.location='" + reverse("ivrequeststatus") + "';</script>")
        
        recipient_email = company.companyemail  
        subject = "Confirmation of Industrial Visit Request"
        body = f"""
        Dear {company.companyname},

        We are pleased to confirm our Industrial Visit request to your esteemed company.

        College Name: {college.collegename}
        No. of Students: {req.noofstudents}
        Scheduled Date: {req.requireddate}

        Thank you for your cooperation. Please let us know if any further details are required.

        Best Regards,  
        {college.collegename}  
        """

        # Email Credentials (Avoid Hardcoding in Production)
        EMAIL_HOST_USER = "ajmalanas516@gmail.com"
        EMAIL_HOST_PASSWORD = "sutg zrcm lzmh kveu"

        # Send Email
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_HOST_USER
        msg["To"] = recipient_email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                smtp.send_message(msg)
        except Exception as e:
            print("Email sending failed:", e)
            return HttpResponse("<script>alert('Email sending failed. Please try again.'); window.location='" + reverse("ivrequeststatus") + "';</script>")

        return HttpResponse(
            "<script>alert('Successfully Confirmed & Email Sent'); window.location='" + reverse("ivrequeststatus") + "';</script>"
        )
    else:
        return HttpResponse("<script>alert('Session Expired! Please login again'); window.location='/login';</script>")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def changepassword(request):
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
                        "<script>alert('Successfully updated!!'); window.location='" + reverse("collegeindex") + "';</script>")

                else:
                    return HttpResponse(
                        "<script>alert('Password Mismatch !!');window.location='" + reverse("changepassword") + "';</script>")
            else:
                return HttpResponse(
                    "<script>alert('Invalid Username or Password!!');window.location='" + reverse("changepassword") + "';</script>")

        return render(request, "college/changepassword.html")
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

