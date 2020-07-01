from django.core.management.base import BaseCommand
from ktGuide.models import Army, Ability, Specialist, Weapon, Unit

import json

def load_army(army):
    all_army = Army.objects.all()
    if not Army.objects.filter(name=army['name']):
        new_army = Army(name=army['name'], bio=army['bio'])
        new_army.save()
    print(all_army)

def load_specialist(specialist):
    all_specialist = Specialist.objects.all()
    if not Specialist.objects.filter(name=specialist['name']):
        new_specialist = Specialist(name=specialist['name'])
        new_specialist.save()
    print(all_specialist)

def load_weapon(weapon):
    all_weapons = Weapon.objects.all()
    if not Weapon.objects.filter(name=weapon['name']):
        new_weapon = Weapon(army=Army(), name=weapon['name'], weapon_range=weapon['range'], weapon_type=weapon['type'], s=weapon['s'], ap=weapon['ap'], d=weapon['d'], abilities=weapon['abilities'], pts=weapon['pts'])
        new_weapon.army = Army.objects.get(name=weapon['army'])
        new_weapon.save()

def load_ability(ability):
    if not Ability.objects.filter(name=ability['name']):
        new_ability = Ability(name=ability['name'], description=ability['description'])
        new_ability.save()

def load_unit(unit):
    all_units = Unit.objects.all()
    if not Unit.objects.filter(name=unit['name']):
        new_unit = Unit(name=unit['name'], m=unit['m'], ws=unit['ws'], bs=unit['bs'], s=unit['s'], t=unit['t'], w=unit['w'], a=unit['a'], ld=unit['ld'], sv=unit['sv'], max_units=unit['max'], point_value=unit['pts'])
        new_unit.army = Army.objects.get(name=unit['army'])
        new_unit.save()
        for i in range(len(unit['weapons'])):
            new_unit.weapons_list.add(Weapon.objects.get(name=unit['weapons'][i]))
        for i in range(len(unit['abilities'])):
            new_unit.ability_list.add(Ability.objects.get(name=unit['abilities'][i]))
        for i in range(len(unit['specialists'])):
            new_unit.specialist_list.add(Specialist.objects.get(name=unit['specialists'][i]))
        new_unit.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('ktGuide/management/commands/armies.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        print(data)
        for i in range(len(data['army'])):
            load_army(data['army'][i])
        for i in range(len(data['specialists'])):
            load_specialist(data['specialists'][i])
        for i in range(len(data['weapons'])):
            load_weapon(data['weapons'][i])
        for i in range(len(data['abilities'])):
            load_ability(data['abilities'][i])
        for i in range(len(data['units'])):
            load_unit(data['units'][i])
        