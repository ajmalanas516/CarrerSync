from django.urls import path
from companyapp import views

urlpatterns = [
    # path('company/', company.site.urls),

    path('companyindex',views.companyindex,name='companyindex'),
    path('internshipregister',views.internshipregister,name='internshipregister'),
    path('internshipregister_process', views.internshipregister_process, name='internshipregister_process'),
    path('viewinternship',views.viewinternship,name='viewinternship'),
    path('deleteinternship/<internshipid>',views.deleteinternship,name='deleteinternship'), 
    path('editinternship/<internshipid>',views.editinternship,name='editinternship'),
  

    path('viewvisitrequest/',views.viewvisitrequest,name='viewvisitrequest'),
    path('iv_viewmore/<id>',views.iv_viewmore,name='iv_viewmore'),
    path('AcceptRequest/<id>',views.AcceptRequest,name='AcceptRequest'),
    path('RejectRequest/<id>',views.RejectRequest,name='RejectRequest'),
    
    path('viewinternshiprequest/',views.viewinternshiprequest,name='viewinternshiprequest'),
    path('internship_viewmore/<id>',views.internship_viewmore,name='internship_viewmore'),
    path('AcceptRequest2/<id>',views.AcceptRequest2,name='AcceptRequest2'),
    path('RejectRequest2/<id>',views.RejectRequest2,name='RejectRequest2'),
    path('enrolled-students/', views.view_enrolled_students, name='view_enrolled_students'),



    path('companyprofile',views.companyprofile,name='companyprofile'),
    path('editcompany',views.editcompany,name='editcompany'),
    path('companychangepassword',views.companychangepassword,name='companychangepassword'),
    path('logout',views.logout,name='logout'),
    






]