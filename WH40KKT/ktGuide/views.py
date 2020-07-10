from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserForm

def index(request):
    context = {
        'message': 'CHAD'
    }
    return render(request, 'ktGuide/index.html', context)

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("logging in...")
            return HttpResponseRedirect(reverse('ktGuide:index'))
        else:
            return render(request, 'ktGuide/login_page.html', {'message':'Username or Password is incorrect'})
    context = {}
    return render(request, 'ktGuide/login_page.html', context)

def logout_page(request):
    logout(request)
    print('logging out...')
    return HttpResponseRedirect(reverse('ktGuide:login_page'))

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