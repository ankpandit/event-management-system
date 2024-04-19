from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def index(request):
    return render(request ,'vendor.html')

def signin(request):
    if(request.method == "POST"):
        user = request.POST.get('username') 
        password = request.POST.get('password')
        print(user,"    ",password)
        auth = authenticate(username =user,password=password)
        print(auth)
        if(auth is not None):
            print("user Authenticated !!!") 
            login(request,auth)
            return redirect('/vendor')
        print("******* \n user not authenticated \n*******")
    return render(request ,'vendorSignin.html')

