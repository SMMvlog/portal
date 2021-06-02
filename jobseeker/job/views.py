from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import UserSign,RecruiterSign
# Create your views here.
def home(request):
    return render(request,'home.html')

def AdminLogin(request):
    loginu = ""
    if request.user.is_authenticated:
        loginu = "no"
        return render(request,'home.html',{"loginu": loginu})
    else:
       return render(request,'admin_login.html')

def UserLogin(request):
    error = ""
    loginu = ""
    if request.user.is_authenticated:
        loginu = "no"
        return render(request,'home.html',{"loginu": loginu})
    elif request.method=="POST":
        username = request.POST['username']
        password = request.POST['pass']
        try:
            user = authenticate(username=username, password=password)
            if user:
                user1=UserSign.objects.get(user=user)
                if user1.type == "Student":
                    login(request,user)
                    error = "no"
                else:
                    error = "yes"
            else:
                error = "yes"    
        except Exception:
            error = "yes"
             
    return render(request,'user_login.html',{'error':error})

class Recruitersign(View):
    def get(self,request):
        return render(request,'recruitersign.html')
    
    def post(self,request):
        error = ""
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['pass']
        gender = request.POST['gender']
        i = request.FILES['image']
        company = request.POST['com'] 
        try:
           user = User(first_name=fname,last_name=lname,username=email,password=password)
           if User.objects.filter(username = email):
               error = "already"
               return render(request,'recruitersign.html',{'error':error})
           else:
             user.save()
           RecruiterSign.objects.create(user=user,mobile=mobile,gender=gender,image=i,company=company,type="Recruiter",status="Panding")
           error = "no"
        except Exception:
                error = "yes"
        return render(request,'recruitersign.html',{'error':error})


def RecruiterLogin(request):
    return render(request,'recruiter_login.html')

def Userlog(request):
       logout(request)
       return redirect('userlogin')

class UserSignup(View):
    def get(self,request):
        return render(request,'user_signup.html')

    def post(self,request):
        error = ""
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['pass']
        gender = request.POST['gender']
        i = request.FILES['image']
        try:
            user = User(first_name=fname,last_name=lname,username=email,password=password)
            if User.objects.filter(username = email):
               error = "already"
               return render(request,'user_signup.html',{'error':error})
            else:
               user.save()
            UserSign.objects.create(user=user,mobile=mobile,gender=gender,image=i,type="Student")
            error = "no"

        except Exception:
            error = "yes"
        return render(request,'user_signup.html',{'error': error})

def Userhome(request):
    users = UserSign.objects.all()
    return render(request,'user_home.html',{'users':users})