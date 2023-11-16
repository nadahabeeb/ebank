from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Services
# Create your views here.
def home(request):
    obj=Services.objects.all()
    return render(request,'index.html',{'obj':obj})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password doesnt match")
            return redirect('register')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('apply')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def apply(request):
    return render(request,'apply.html')

def app_form(request):
    if request.method=='POST':
        messages.info(request,"Application accepted. ")
    return render(request,'form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')