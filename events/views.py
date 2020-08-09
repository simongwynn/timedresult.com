from django.shortcuts import render, get_object_or_404
from .models import Event
from datetime import timedelta,date

def home(request):
    enddate = date.today() + timedelta(days=5)
    todaydate= date.today()
    currentevents = Event.objects.order_by('datestart').filter(datestart__lte=date.today(), datefinish__lte=enddate)
    upcomingevents = Event.objects.order_by('datestart').filter(datestart__gt=date.today())[:3]
    return render(request, 'events/home.html', {'currentevents':currentevents, 'upcomingevents':upcomingevents, 'todaydate':todaydate})

def road(request):
    events = Event.objects.order_by('-datestart').filter(discipline='RD',datestart__lte=date.today())
    return render(request, 'events/RD.html', {'events':events})

def track(request):
    events = Event.objects.order_by('-datestart').filter(discipline='TR',datestart__lte=date.today())
    return render(request, 'events/TR.html', {'events':events})

def cyclocross(request):
    events = Event.objects.order_by('-datestart').filter(discipline='CX',datestart__lte=date.today())
    return render(request, 'events/CX.html', {'events':events})

def mountainbike(request):
    events = Event.objects.order_by('-datestart').filter(discipline='MTB',datestart__lte=date.today())
    return render(request, 'events/MTB.html', {'events':events})

def gravel(request):
    events = Event.objects.order_by('-datestart').filter(discipline='MTB',datestart__lte=date.today())
    return render(request, 'events/GR.html', {'events':events})

def detail(request, page_id):
    result = get_object_or_404(Event, pk=page_id)
    return render(request, 'events/detail.html',{'result':result})

def startlist(request, page_id):
    result = get_object_or_404(Event, pk=page_id)
    return render(request, 'events/startlist.html',{'result':result})

def results(request, page_id):
    result = get_object_or_404(Event, pk=page_id)

    data = Event.objects.get(pk=page_id)
    if data.stage0 == True:
        x = 0
    else:
        x = 1
    stages = ''
    for i in range(data.stages):
        stages += str(x)
        x += 1
    return render(request, 'events/results.html',{'result':result, 'stages':stages})
