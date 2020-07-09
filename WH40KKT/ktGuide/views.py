from django.shortcuts import render
from django.http import HttpResponse
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
    else:
        form = CustomUserForm()
    context = {'form':form}
    return render(request, 'ktGuide/register.html', context)

def myprofile(request):
    context = {}
    return render(request, 'ktGuide/myprofile.html', context)