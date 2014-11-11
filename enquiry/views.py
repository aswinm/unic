from django.shortcuts import render,redirect
from enquiry.models import Enquiry
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout

def index(request,text=""):
    return render(request,'index.html',{'text':text})

def store(request):
    if request.method == "POST":
        details = request.POST
        e = Enquiry.objects.create(
                name = details["name"],
                email = details["email"],
                subject = details["subject"],
                desc = details["desc"]

                )
        e.save()
        text = "We have recieved your request. We will get back to you as soon as possible"
        return HttpResponseRedirect("/?submit=true")
    else:
        return HttpResponseRedirect("/")
        


def enquiries(request):
    if request.user.is_authenticated:
        enq = Enquiry.objects.all()
        return render(request,"enq.html",{'enquiries':enq})
    else:
        return HttpResponseRedirect("/login")

def logon(request):
    if request.method == "POST":
        pass
    else:
        return render(request,"login.html")

def verify(request):	
    return render(request,'verifyforzoho.html')

#Create your views here.
