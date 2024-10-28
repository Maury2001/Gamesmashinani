from django.shortcuts import render, redirect
from .models import Fixture, Pool, Team, Region
from .forms import *
from .filter import TeamFilter , FixtureFilter

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


def Base(request):
    pools = Pool.objects.all()

    context={
        'pools':pools

    }

    return render(request, "Games/base.html", context)


def Dash(request):

    region = Region.objects.all()
    pool = Pool.objects.all()
    kteam = Team.objects.filter(pool__region__name='KIAMBU')
    teams= Team.objects.all().order_by('-points')
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
            return redirect('pool_idpoolform')
        
    context= {
        'form':form
    }

    return render(request, 'Games/poolform.html', context)

def KiambuTable(request):

    kiambuA = Team.objects.filter(pool__name='k pool A').order_by('-points')
    KiambuB = Team.objects.filter(pool__name='k pool B').order_by('-points')
    murangaA = Team.objects.filter(pool__name='m pool A').order_by('-points')
    murangaB = Team.objects.filter(pool__name='m pool B').order_by('-points')
    

    context={
        'kiambuA':kiambuA,
        'kiambuB':KiambuB,
        'murangaA':murangaA,
        'murangaB':murangaB
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


def Table(request, pk):
    pool = Pool.objects.get(id=pk)
    teams = Team.objects.filter(pool=pool).order_by('-points')  # Assuming Team has a 'pool' foreign key

    # Apply filtering on the filtered teams
    myfilter = TeamFilter(request.GET, queryset=teams)
    teams = myfilter.qs

    context = {
        'teams': teams,
        'pool': pool
    }

    return render(request, "Games/pooltable.html", context)

def Fix(request):
    
    fixtures= Fixture.objects.all()
    upcoming= Fixture.objects.filter(status="upcoming")
    played= Fixture.objects.filter(status="played")
    live= Fixture.objects.filter(status="live")

    # Filter fixtures where both home and away teams belong to the same pool
    
    myfilter = FixtureFilter(request.GET, queryset=fixtures)
    fixtures = myfilter.qs

    context = {
        'fixtures': fixtures,
        'upcoming': upcoming,
        'myfilter':myfilter,
        'live':live,
        'played':played,

    }

    return render(request, "Games/fixture.html", context)
