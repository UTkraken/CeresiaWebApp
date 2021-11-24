from django.shortcuts import render

from Ceresia.models import Hike, History, Species
from .filters import HikeFilter, CerescopeFilter


def hikes(request):
    hikes_list = Hike.objects.all()
    hike_filter = HikeFilter(request.GET, queryset=hikes_list)
    hikes_list = hike_filter.qs

    context = {
        'hikes': hikes_list,
        'hike_filter': hike_filter
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
    species_filter = CerescopeFilter(request.GET, queryset=species)
    species = species_filter.qs
    context = {
        'species': species,
        'species_filter' : species_filter
    }
    return render(request, 'ceresia/cerescope.html', context)


def achievements(request):
    return render(request, 'ceresia/achievements.html')


def login(request):
    return render(request, 'ceresia/login.html')
