from django.core.management.base import BaseCommand
from ktGuide.models import Army, Ability, Specialist, Weapon, AbilityList, SpecialistList, WeaponList, Unit

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

def load_weapons(weapon):
    all_weapons = Weapon.objects.all()
    if not Weapon.objects.filter(name=weapon['name']):
        new_weapon = Weapon(army=Army(), name=weapon['name'], weapon_range=weapon['range'], weapon_type=weapon['type'], s=weapon['s'], ap=weapon['ap'], d=weapon['d'], abilities=weapon['abilities'], pts=weapon['pts'])
        new_weapon.army = Army.objects.get(name=weapon['army'])
        new_weapon.save()

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
            load_weapons(data['weapons'][i])
        