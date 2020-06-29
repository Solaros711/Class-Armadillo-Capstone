from django.core.management.base import BaseCommand
from ktGuide.models import Army, Ability, Specialist, Weapon, AbilityList, SpecialistList, WeaponList, Unit

import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('ktGuide/management/commands/armies.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        print(data)    
        