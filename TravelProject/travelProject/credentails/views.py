from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def registeration(request):
    if request.method == "POST":
        userName = request.POST['username']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conPassword = request.POST['password1']

        if password == conPassword:
            if User.objects.filter(username=userName).exists():
                messages.info(request,"Username already used")
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect('registeration')
            else:
                user = User.objects.create_user(username=userName,password=password,first_name=firstName,last_name=lastName,email=email)

                user.save()
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"Password Not Matched")
            print("Password Not Matching")
            return redirect('registeration')

        return redirect('/')

    return render(request,"register.html")

def login(request):
    if request.method == "POST":
        userName = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=userName,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')