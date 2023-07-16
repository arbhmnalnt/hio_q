from django.shortcuts import render
from .models import *
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



@login_required
@csrf_exempt
def saveData(request):
    import json
    msg     = 'erorr happens '
    data    = ''
    if request.method == 'POST':
        data = json.loads(request.body)
        #  {ayadaId: "1", clientName: "", clientNum: "", lawOrentity: "", waitNo: 1
        ayadaId= data['ayadaId']
        ayada = Ayada.objects.get(pk=ayadaId)
        clientName= data['clientName']
        clientNum=data['clientNum']
        lawOrentity=data['lawOrentity']
        waitNo=data['waitNo']
        newVisit = Visit.objects.create(name=clientName, clientNum=clientNum,lawOrentity=lawOrentity, waitNo=waitNo, ayada=ayada, created_by=request.user)

        print("newVisit id => ", newVisit.id)
    response = {'msg':msg, 'data':data}
    return JsonResponse(response)


def getLastAyadaCount(request, pk):
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%Y-%m-%d")

    # Get the current time shift as AM or PM
    current_shift = now.strftime("%p")

    # Check if any visit was created at the same date and in the same shift as the current time
    ayadaPk = Ayada.objects.get(pk=pk)
    lastAyadaVisit = Visit.objects.filter(
        Q(created_at__date=current_date) & Q(ayada=ayadaPk) &
        (Q(created_at__hour__lt=12) if current_shift == 'AM' else Q(created_at__hour__gte=12))
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
    hour = now.hour
    if hour < 12:
        shift = "الفترة الصباحية"
    else:
        shift = "الفتؤة المسائية"
    data = {
        'date':current_date,
        'time':current_time,
        'shift':shift,
    }
    return JsonResponse(data)

def mainPage(request):
    
    ayadat = Ayada.objects.all()
    context = {
        'ayadat':ayadat
    }
    return  render(request, 'archieve/main.html', context)