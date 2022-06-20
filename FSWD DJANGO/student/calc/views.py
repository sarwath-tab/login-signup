from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
    x=2
    x=x+1
    x=x+5
    return render(request,'index.html')

def abc(request):
    return render(request,'index2.html')

def login(request):
    return render(request,'index3.html')
  
