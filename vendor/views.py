from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from vendor.models import vendor,services
# Create your views here.

def index(request):

    if(request.method == "POST"):
        print("service = " , request.POST.get("service"))
        serv = services(vendorname=request.user,serviceName=request.POST.get("service") , rate =request.POST.get('rate') ,description =  request.POST.get('description'))
        serv.save()

    print(request.user)
    service = services.objects.filter(vendorname = request.user).values()
    # service = services.objects.all()
    print(service)
    print(service.values())

    data = {
        'services' :service
    }
    return render(request ,'vendor.html',data)

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

def signup(request):
    if(request.method =="POST"):
        user = User.objects.create_user(username=request.POST.get("username"),email=request.POST.get("email"),password=request.POST.get("password"))


def remove(request):
    print(request.get('service'))
    return render(request , 'vendor.html')
