from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from art.models import *

from art.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
   
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
       
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request,"Registred Successfully")
            return redirect('/login')
    context = {'form':form}
    return render(request,"auth/register.html",context)



def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already Loggedin")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            passwrd = request.POST.get('pswd')
            user = authenticate(request,username =name, password = passwrd)
            if user is not None:
                
                login(request,user)
                messages.success(request,"Login successful")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password")
                return redirect('/login')

    return render(request,"auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect('/')


