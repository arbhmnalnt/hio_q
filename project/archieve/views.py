from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import JsonResponse

# Create your views here.

def getDateTime(request):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%Y-%m-%d")
    data = {
        'date':current_date,
        'time':current_time,
    }
    return JsonResponse(data)

def mainPage(request):
    
    ayadat = Ayada.objects.all()
    context = {
        'ayadat':ayadat
    }
    return  render(request, 'archieve/main.html', context)