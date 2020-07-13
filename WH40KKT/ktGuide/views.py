from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserForm
from .models import Army, Unit, Weapon, Specialist, Guide, GuideUnit
from django.contrib.auth.decorators import login_required

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

@login_required
def myprofile(request):
    context = {}
    return render(request, 'ktGuide/myprofile.html', context)

@login_required
def make_guide(request):
    context = {
        'army_list': Army.objects.order_by('name')
    }
    return render(request, 'ktGuide/makeguide.html', context)

@login_required
def get_units(request):
    army_id = request.GET['army_id']
    army = Army.objects.get(id=army_id)

    units = Unit.objects.filter(army_id=army_id)
    units = units.order_by('name')
    units_json = []
    for unit in units:
        units_json.append({
            'id': unit.id,
            'name': unit.name,
        })
        print(units_json)
    return JsonResponse({'army': army.id, 'units': units_json})

@login_required
def get_unit_stuff(request):
    unit_id = request.GET['unit_id']
    unit = Unit.objects.get(id=unit_id)

    weapons = unit.weapons_list.order_by('name')
    specialists = unit.specialist_list.order_by('name')

    weapons_json = []
    specialists_json = []

    for weapon in weapons:
        weapons_json.append({
            'id': weapon.id,
            'name': weapon.name
        })

    for specialist in specialists:
        specialists_json.append({
            'id': specialist.id,
            'name': specialist.name
        })

    return JsonResponse({'unit': unit.id, 'weapons': weapons_json, 'specialists': specialists_json})

@login_required
def get_presentable(request):
    unit_name = request.GET['unit_name']
    unit_id = request.GET['unit_id']
    unit_weapon_id = request.GET['unit_weapon_id']
    unit_specialist_id = request.GET['unit_specialist_id']

    unit = Unit.objects.get(id=unit_id).name
    weapon = Weapon.objects.get(id=unit_weapon_id).name
    specialist = Specialist.objects.get(id=unit_specialist_id).name

    return JsonResponse({'name': unit_name, 'unit': unit, 'weapon': weapon, 'specialist':specialist})

def view_guide(request):
    context = {}
    return render(request, 'ktGuide/viewguide.html', context)