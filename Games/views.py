from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filter import TeamFilter 

# Create your views here.
def Home(request):
    kpools = Pool.objects.filter(region__name='KIAMBU')
    mpools = Pool.objects.filter(region__name='MURANGA')

    fixtures = Fixture.objects.all()


    context={
        'kpools':kpools,
        'mpools':mpools,
        'fixtures':fixtures
    }


    return render(request, 'Games/Home.html', context)



def Dash(request):

    region = Region.objects.all()
    pool = Pool.objects.all()
    kteam = Team.objects.filter(pool__region__name='KIAMBU')
    teams= Team.objects.all()
    kpools = Pool.objects.filter(region__name='KIAMBU')
    mpools = Pool.objects.filter(region__name='MURANGA')
    murangaA = Team.objects.filter(pool__name='m pool A').order_by('-points')
    murangaB = Team.objects.filter(pool__name='m pool B').order_by('-points')
    kiambuA = Team.objects.filter(pool__name='k pool A').order_by('-points')
    KiambuB = Team.objects.filter(pool__name='k pool B').order_by('-points')

    fixture = Fixture.objects.all()

    myfilter = TeamFilter(request.GET, queryset=teams)
    teams = myfilter.qs

    

    context={
        'region':region,
        'pool':pool,
        'kteam':kteam,
        'teams':teams,
        'kpools':kpools,
        'mpools':mpools,
        'muranga': murangaA,
        'murangaB': murangaB,
        "kiambuA":kiambuA,
        "kiambuB": KiambuB,
        "fixture":fixture,
        "myfilter":myfilter
    }

    return render(request, 'Games/dashboard.html', context)

def RegionAdj(request):
    form = RegionForm()
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regionform')
        
    context= {
        'form':form
    }

    return render(request, 'Games/regionform.html', context)

def TeamAdj(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teamform')
        
    context= {
        'form':form
    }

    return render(request, 'Games/teamform.html', context)

def PoolAdj(request):
    form = PoolForm()
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poolform')
        
    context= {
        'form':form
    }

    return render(request, 'Games/poolform.html', context)

def KiambuTable(request):

    kiambuA = Team.objects.filter(pool__name='k pool A').order_by('-points')
    KiambuB = Team.objects.filter(pool__name='k pool B').order_by('-points')

    context={
        'kiambuA':kiambuA,
        'kiambuB':KiambuB
    }


    return render(request, 'Games/kiambutable.html', context)

def MurangaTable(request):

    murangaA = Team.objects.filter(pool__name='m pool A').order_by('-points')
    murangaB = Team.objects.filter(pool__name='m pool B').order_by('-points')
    


    context={
        'murangaA':murangaA,
        'murangaB':murangaB
    }


    return render(request, 'Games/murangatable.html',context)