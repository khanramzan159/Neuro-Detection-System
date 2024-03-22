import re
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from hashlib import sha256
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.template.loader import get_template
from django.views import View
from .forms import RegisterForm
from .models import User,Admin
from .forms import LoginForm

def home(request):
    # if request.session.has_key('login'):
    #     return redirect(home)
    
    return render (request, 'home.html')




def register(request):
    if request.session.has_key('login'):
        return redirect(home)
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            passenc = form.cleaned_data['password']
            password = sha256(passenc.encode()).hexdigest()
            user = User.objects.filter(email=email)
            if user:
                messages.error(request, 'User already exists! Do LogIn')
                return redirect(login)
            else:
                form.save()
                request.session['login'] = 1
                return redirect(home)
    else:
        form = RegisterForm()

    return render (request, 'register.html', {'form': form})


def login(request):
    if request.session.has_key('login'):
        return redirect(home)
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            passenc = form.cleaned_data['password']
            password = sha256(passenc.encode()).hexdigest()
            user = User.objects.filter(email=email, password=password)
            if not user:
                messages.error(request,'Invalid Credentials')
                return redirect(login)
            else:
                messages.success(request, 'Successfully Logged in')
                request.session['login'] = 1
                return redirect(home)
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout(request):
    if 'login' in request.session:
        del request.session['login']
    if 'admin' in request.session:
        del request.session['admin']
    return redirect(login)


def project(request):
    pass

def admin(request):
    if request.session.has_key('user'):
        return redirect(home)
    if request.session.has_key('admin'):  
        if request.session.has_key('deleterr'):
            messages.error(request, 'no such user to delete!') 
            del request.session['deleterr']
        if request.session.has_key('deletesucc'):
            messages.success(request, 'User deleted successfully!')   
            del request.session['deletesucc']    
        if request.session.has_key('updateuser'):
            messages.success(request, 'User updated successfully!')   
            del request.session['updateuser']
        if request.session.has_key('createuser'):
            messages.success(request, 'User added successfully!')   
            del request.session['createuser']   
        if request.session.has_key('searchuser'):
            messages.error(request, 'No such user!')   
            del request.session['searchuser']   
        users = User.objects.all()            
        return render(request, 'admin.html', {'dets': users})
    elif request.POST:
            usern = request.POST.get('username')
            passw = request.POST.get('password')
            # passwenc = sha256(passw.encode()).hexdigest()
            admins = Admin.objects.filter(username=usern,password=passw)
            if admins:
                request.session['admin'] = 1
                return redirect(admin)
            else:    
                return render(request, 'admin-login.html', {'error': 'Invalid credentials!'})      
    else:    
        return render(request, 'admin-login.html')