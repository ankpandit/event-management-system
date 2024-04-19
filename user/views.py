from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request , 'user.html')

def servicelist(request):
    return render(request , 'serviceList.html')