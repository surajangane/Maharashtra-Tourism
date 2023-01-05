from django.shortcuts import redirect, render,HttpResponse
from .models import Booking,contact
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request,'index.html')

def book(request):
    if request.method=='POST':
        name=request.POST['name']
        where=request.POST['where']
        guest=request.POST['guest']
        arrivals=request.POST['arrivals']
        leaving=request.POST['leaving']
        
        b1=Booking.objects.create(name=name,where=where,guest=guest,arrivals=arrivals,leaving=leaving)
        b1.save()
    return render(request,'book.html')

def editform(request,rid):
    if request.method=="POST":
        #id=request.POST['id']
        name=request.POST['name']
        where=request.POST['where']
        guest=request.POST['guest']
        arrivals=request.POST['arrivals']
        leaving=request.POST['leaving']
        
        b1=Booking.objects.filter(id=rid)
        b1.update(name=name,where=where,guest=guest,arrivals=arrivals,leaving=leaving)
        return redirect('/editform')
    rec=Booking.objects.get(id=rid)
    content={}
    content['data']=rec
    return render(request,'editform.html',content)
    #return redirect('/my_booking')

def delete(request,rid):
    b1=Booking.objects.get(id=rid)
    b1.delete()
    return redirect('/my_booking')

def packages(request):
    return render(request,'packages.html')

def gallery(request):
    return render(request,'gallery.html')

def Contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        subject=request.POST['subject']
        message=request.POST['message']
        
        c1=contact.objects.create(name=name,email=email,number=number,subject=subject,message=message)
        c1.save()
    return render(request,'contact.html')

def my_booking(request):
    # q1=Q(id=id)
    # records=Booking.objects.filter(q1)
    records=Booking.objects.all()
    content={'data':records}
    return render(request,'my_booking.html',content)


def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            if u:
                login(request,u)#this function start session for that user
                return redirect('/')
    else:
        fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})  

def user_logout(request):
    logout(request)# this is use to distroy session
    return redirect('/login')

def register(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            #return HttpResponse("user register successfully")
            return redirect('/login')
    else:
        fm=UserCreationForm()
        return render(request,'register.html',{'form':fm})

   
# get and set session
def setsession(request):
    request.session['user']='itvedant-django'
    return render(request,'setsession.html')

def getsession(request):
    data=request.session['user']
    return render(request,'getsession.html',{'d':data})
