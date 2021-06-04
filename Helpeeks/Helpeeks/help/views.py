from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SignUp
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.



def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # phone = request.POST['phone']

        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = username
        myuser.save()
        messages.success(request, " Your EasyShop account has been successfully created")
        return redirect('/signup')
    return render(request,'open.html')


def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('/signup')
        else:
            messages.warning(request, "Invalid Credentials, please try again!")
            return HttpResponse("<h3>Invalid Credentials, please try again!</h3><br><a href='/signup'> Click here</a>")
    return HttpResponse("404 - Not Found")
