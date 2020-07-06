from django.shortcuts import render
from django.http import HttpResponse

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
    context = {}
    return render(request, 'ktGuide/register.html', context)