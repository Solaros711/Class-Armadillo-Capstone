from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserForm
from .models import Army, Unit, Weapon, Specialist, Guide, GuideUnit, Comment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.template import loader
import datetime
import json

def index(request):
    page = request.GET.get('page',1)
    template = loader.get_template('ktGuide/index.html')
    if Guide.objects.count():
        list_of_guides = Guide.objects.order_by('title')
        paginator = Paginator(list_of_guides, 20)
        context = {
            'list_of_guides': list_of_guides
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {
            'message': 'There are no guides to view!'
        }
        return HttpResponse(template.render(context, request))
    

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

@login_required
def submit_guide(request):
    data = json.loads(request.body)
    date = datetime.datetime.now()

    army_id = data['army']
    title = data['title']
    text = data['text']

    guide = Guide(author=request.user, army=Army.objects.get(id=army_id), title=title, guide_desc=text, date_created=date)
    guide.save()

    for unit in data['units']:
        guide_unit = GuideUnit(name=unit['name'], guide=guide, unit=Unit.objects.get(id=int(unit['unit'])), weapon=Weapon.objects.get(id=int(unit['weapon'])), role=Specialist.objects.get(id=int(unit['specialist'])))
        guide_unit.save()

    return HttpResponse(guide.id)

@login_required
def submit_comment(request):
    data = json.loads(request.body)
    author = request.user
    date = datetime.datetime.now()
    comment_text = data['comment']
    guide = Guide.objects.get(id=data['id'])
    
    comment = Comment(author=author, guide=guide, content=comment_text, date_created=date)
    comment.save()

    return HttpResponse(guide.id)


def view_guide(request, guide_id):
    guide = Guide.objects.get(id=guide_id)
    list_of_comments = Comment.objects.filter(guide=guide_id)
    list_of_comments = list_of_comments.order_by('date_created')
    template = loader.get_template('ktGuide/viewguide.html')
    context = {
        'guide': guide,
        'list_of_comments': list_of_comments
    }
    return HttpResponse(template.render(context, request))