from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Icecream(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def base(request):
    return render(request,'base.html')