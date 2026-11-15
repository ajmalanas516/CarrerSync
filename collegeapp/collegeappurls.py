from django.urls import path
from collegeapp import views

urlpatterns = [
    # path('college/', college.site.urls),

    path('collegeindex',views.collegeindex,name='collegeindex'),
    path('search',views.search,name='search'),
    # path('filllocation',views.filllocation,name='filllocation'),
    # path('fillcompanytype',views.fillcompanytype,name='fillcompanytype'),
    path('requestiv/<companyid>',views.requestiv,name='requestiv'),
    path('requestiv_process/', views.requestiv_process, name='requestiv_process'),
    path('ivrequeststatus',views.ivrequeststatus,name='ivrequeststatus'),
    path('collegeprofile',views.collegeprofile,name='collegeprofile'),
    # path('fillcompanytype',views.fillcompanytype,name='fillcompanytype'),
    
    path('fillcompany1',views.fillcompany1,name='fillcompany1'),
    path('filllocationandcompany1',views.filllocationandcompany1,name='filllocationandcompany1'),
    path('fillcompanytypeandcompany1',views.fillcompanytypeandcompany1,name='fillcompanytypeandcompany1'),


    path('collegeprofile',views.collegeprofile,name='collegeprofile'),
    path('editcollegeprofile',views.editcollegeprofile,name='editcollegeprofile'),
    path('cancel<id>',views.cancel,name='cancel'),
    path('confirm<id>',views.confirm,name='confirm'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('logout',views.logout,name='logout'),


]