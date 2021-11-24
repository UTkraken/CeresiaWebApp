from django.shortcuts import render

from Ceresia.models import Hike, History, Species


def hikes(request):
    hikes = Hike.objects.all()
    context = {
        'hikes': hikes
    }
    return render(request, 'ceresia/hikes.html', context)


def history(request):
    history = History.objects.all()
    context = {
        'history': history
    }
    return render(request, 'ceresia/history.html', context)


def cerescope(request):
    species = Species.objects.all()
    context = {
        'species': species
    }
    return render(request, 'ceresia/cerescope.html', context)


def achievements(request):
    return render(request, 'ceresia/achievements.html')


def login(request):
    return render(request, 'ceresia/login.html')
