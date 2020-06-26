from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'CHAD'
    }
    return render(request, 'ktGuide/index.html', context)