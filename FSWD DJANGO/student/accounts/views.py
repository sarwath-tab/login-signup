from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("logged in")
            return redirect('/')
    else:   
        return render(request,'login.html')

def signup(request):
    if request.method =='POST':
       firstName = request.POST['firstName']
       print(firstName)
       lastName= request.POST['lastName']
       username=request.POST['username']
       email= request.POST['email']
       password = request.POST['password']
       if User.objects.filter(username = username).first():

            return redirect("/")
       user = User.objects.create_user(username=username,email=email,password=password)

       print("user created")
       return render(request,'/')
    else:
       return render(request,'signup.html')   

def accounts(request):
    return render(request,"this is account page")
    
