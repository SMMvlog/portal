from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminlogin/', views.AdminLogin, name='adminlogin'),
    path('userlogin/', views.UserLogin, name='userlogin'),
    path('recruiterlogin/', views.RecruiterLogin, name='recruiterlogin'),
    path('usersignup/', views.UserSignup.as_view(), name='usersignup'),
    path('recruitersign/', views.Recruitersign.as_view(), name='recruitersign'),
    path('userlog/', views.Userlog, name='userlog'),
    path('recruitersign/', views.Recruitersign, name='recruitersign'),
    path('userhome/', views.Userhome, name='userhome'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)