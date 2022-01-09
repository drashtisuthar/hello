from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import member,Books,pro
from .forms import memberform,bookform
from django.db.models import Q

# Create your views here.
def hey(request):
    return HttpResponse("hello world good")

def a(request):
    return render(request,'a.html')
  
def register(request):
    if request.method=="POST":
        obj=member()
        obj.username=request.POST['name']
        obj.email=request.POST['email']
        obj.phn=request.POST['phn']
        obj.password=request.POST['pass']
        obj.save()
    return render(request, 'register.html')        

def signin(request):
    if request.method=="POST":
        try:
            v=request.POST['name']
            m = member.objects.get(username=v)
            print(m)
            
            if m.password == request.POST['pass']:
                return HttpResponseRedirect('/fine/home/')

            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password </a></h2>")
        except:
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def info(request):
    return render(request,'info.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    q=Books.objects.all()
    try:
        q =request.GET.get('search')
        print(q)
    except:
        q = None
    if q:
        print("ffg")
        book1= Books.objects.filter(Q(bookname__icontains=q) | Q(discription__icontains=q) | Q(price__icontains=q))
        data = {
            'book' : book1,
        }
    else:
        data={}
    return render(request,'index.html',data)   

def book(request):
    b=book.objects.all()
    return render(request,'book.html',{'b':b})

def booknew(request):
    b=bookform(request.POST)
    if b.is_valid():
        b.save()
    return render(request,'booknew.html',{'form':b}) 

def bookview(request,pk):
    o=get_object_or_404(Books,pk=pk)
    return render(request,'bookview.html',{'b1':o})

def proview(request,pk):
    obj=get_object_or_404(pro,ok=ok)
    return render(request,'proview.html',{'obj':obj})