from django.core.management.base import BaseCommand
# from ktGuide.models import 

import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("it worked!")