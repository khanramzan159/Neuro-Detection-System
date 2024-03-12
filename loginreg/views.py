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
from .models import User

def home(request):
    if not request.session.has_key('login'):
        return redirect(register)
    
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
                return render(request, 'loginreg/register.html')
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

def logout(request):
    request.session.flush()
    return redirect(home)

def project(request):
    pass