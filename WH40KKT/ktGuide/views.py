from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm

def index(request):
    context = {
        'message': 'CHAD'
    }
    return render(request, 'ktGuide/index.html', context)

def login(request):
    context = {}
    return render(request, 'ktGuide/login.html', context)

def login_user(request):
    context = {}
    return render(request, 'ktGuide/login.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'message':'Account created!'}
            return render(request, 'ktGuide/login.html', context)
    else:
        form = CustomUserForm()
    context = {'form':form}
    return render(request, 'ktGuide/register.html', context)

def myprofile(request):
    context = {}
    return render(request, 'ktGuide/myprofile.html', context)

def make_guide(request):
    context = {}
    return render(request, 'ktGuide/makeguide.html', context)

def view_guide(request):
    context = {}
    return render(request, 'ktGuide/viewguide.html', context)