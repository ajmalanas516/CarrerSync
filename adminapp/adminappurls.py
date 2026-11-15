from django.urls import path
from adminapp import views
from .views import ExportProfitReport, ExportStudentReport, StudentReportView
from .views import ExportExcelCollege





urlpatterns = [
    # path('admin/', admin.site.urls),

    path('adminindex',views.adminindex,name='adminindex'),

    path('district',views.district,name='district'),
    path('deletedistrict/<districtid>',views.deletedistrict,name='deletedistrict'),
    path('district_process',views.district_process,name='district_process'),
    path('viewdistrict',views.viewdistrict,name='viewdistrict'),
    path('editdistrict/<districtid>',views.editdistrict,name='editdistrict'),

    path('location',views.location,name='location'),
    path('location_process',views.location_process,name='location_process'),
    path('viewlocation',views.viewlocation,name='viewlocation'),
    path('filllocation',views.filllocation,name='filllocation'),
    path('deletelocation/<locationid>',views.deletelocation,name='deletelocation'),
    path('editlocation/<locationid>',views.editlocation,name='editlocation'),
    
    path('companytype',views.companytype,name='companytype'),
    path('companytype_process',views.companytype_process,name='companytype_process'),
    path('viewcompanytype',views.viewcompanytype,name='viewcompanytype'),
    path('deletecompanytype/<companytypeid>',views.deletecompanytype,name='deletecompanytype'),
    path('editcompanytype/<companytypeid>',views.editcompanytype,name='editcompanytype'),


    path('companyverification',views.companyverification,name='companyverification'),
    path('acceptrequest/<companyid>',views.acceptrequest,name='acceptrequest'),
    path('rejectrequest/<companyid>',views.rejectrequest,name='rejectrequest'),

    path('collegeverification',views.collegeverification,name='collegeverification'),
    path('collegeacceptrequest/<collegeid>',views.collegeacceptrequest,name='collegeacceptrequest'),
    path('collegerejectrequest/<collegeid>',views.collegerejectrequest,name='collegerejectrequest'),


    path('paymentview',views.paymentview,name='paymentview'),
    path('pie_chart_companytype',views.pie_chart_companytype,name='pie_chart_companytype'),
    path('piechart_companywiseinternship',views.piechart_companywiseinternship,name='piechart_companywiseinternship'),
    path('piechart_districtwisecompany',views.piechart_districtwisecompany,name='piechart_districtwisecompany'),
    path('piechart_districtwisecollege',views.piechart_districtwisecollege,name='piechart_districtwisecollege'),
    path('piechart_districtwisestudent',views.piechart_districtwisestudent,name='piechart_districtwisestudent'),
    path('piechart_studentinternshipenrolled',views.piechart_studentinternshipenrolled,name='piechart_studentinternshipenrolled'),


    path('ExportExcelCollege', ExportExcelCollege.as_view(), name='ExportExcelCollege'),
    path('ExportExcelCompany', views.ExportExcelCompany.as_view(), name='ExportExcelCompany'),

    path('barchart_companywisevisit',views.barchart_companywisevisit,name='barchart_companywisevisit'),
    path('datewise_report/', ExportProfitReport.as_view(), name='datewise_report'),
    path('logout',views.logout,name='logout'),

    path('StudentReportView/', StudentReportView, name='StudentReportView'),
    path('ExportStudentReport/', ExportStudentReport.as_view(), name='ExportStudentReport'),






]