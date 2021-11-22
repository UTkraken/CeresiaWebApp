from django.shortcuts import render

from Ceresia.models import Hike, History, Species


def hikes(request):
    hikes = Hike.objects.all()
    contexte = {
        'hikes': hikes
    }
    return render(request, 'ceresia/hikes.html', contexte)


def history(request):
    history = History.objects.all()
    contexte = {
        'history': history
    }
    return render(request, 'ceresia/history.html')


def cerescope(request):
    species = Species.objects.all()
    contexte = {
        'species': species
    }
    return render(request, 'ceresia/cerescope.html')
