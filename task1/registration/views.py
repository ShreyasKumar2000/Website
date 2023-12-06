from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def reg(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        password= request.POST['password']
        c_password= request.POST['c_password']
        if password== c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('/registration/credentials')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('/registration/credentials')
            else:
                cred=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                cred.save();
                print("User created")
        else:
            messages.info(request,"password not matched")
            return redirect('/registration/credentials')
        return redirect('/')
    return render(request,"regi.html")

def login(request):
    if request.method == 'POST':
        u_name=request.POST['username']
        pw=request.POST['password']
        person=auth.authenticate(username=u_name,password=pw)
        if person is not None:
            auth.login(request,person)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('/registration/login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')