from django.urls import path
from guestapp import views

urlpatterns = [
    # path('guest/', guest.site.urls),

    path('',views.guestindex,name='guestindex'), 
    path('login',views.login,name='login'),
    path('login_process',views.login_process,name='login_process'),
    path('companyregister',views.companyregister,name='companyregister'),
    path('companyregister_process',views.companyregister_process,name='companyregister_process'),
    path('collegeregister',views.collegeregister,name='collegeregister'),
    path('collegeregister_process',views.collegeregister_process,name='collegeregister_process'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('studentregister_process',views.studentregister_process,name='studentregister_process'),
    path('filllocationnew',views.filllocationnew,name='filllocationnew'),

    path('forgot_password',views.forgot_password,name="forgot_password"),





]