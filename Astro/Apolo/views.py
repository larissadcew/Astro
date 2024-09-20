from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request,'new.html')

def Login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def Eventos(request):
    return render(request,'events.html')

