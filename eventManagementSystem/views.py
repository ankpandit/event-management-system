from django.shortcuts import render,redirect
from django.contrib import messages
# authentication 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.

def home(request):
    if request.user.is_anonymous:
        print("user is anonymous")
        return render(request ,'home.html')

    return render(request ,'home.html')

def signin(request):
    print("LOGIN PAGE >>>>")
    if(request.method=="POST"):
        user = request.POST.get('username') 
        password = request.POST.get('password')
        print(user,"    ",password)
        auth = authenticate(username =user,password=password)
        print(auth)
        if(auth is not None):
            print("user Authenticated !!!") 
            login(request,auth)
            return redirect('/user')
        print("******* \n user not authenticated \n*******")

    return render(request ,'signin.html')

def logout(request):
    logout(request)
    return redirect('/')