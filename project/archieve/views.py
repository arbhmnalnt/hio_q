from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.

def getLastAyadaCount(request, pk):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%Y-%m-%d")

    # Check if any visit was created at the same date and in AM/PM
    lastAyadaVisit = Visit.objects.filter(
        Q(created_at__date=current_date) & 
        (Q(created_at__hour__lt=12) | Q(created_at__hour__gte=12))
    )

    if lastAyadaVisit.exists():
        # Visit exists for current date and AM/PM
        count = lastAyadaVisit.count()
        print("YES => count => ", count)
    else:
        print("NO")
        # Visit does not exist for current date and AM/PM
        # Do something else
        count = 0

    data = {
        'count':count,
        'nextCount':count+1,
    }
    return JsonResponse(data)



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