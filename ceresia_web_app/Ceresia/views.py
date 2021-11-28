from django.shortcuts import render

from Ceresia.models import Hike, History, Species
from .filters import HikeFilter, CerescopeFilter

from Ceresia import fill_database

run_once = 0


def hikes(request):
    global run_once
    if run_once == 0:
        fill_database.generate_data_docker()
        run_once = 1
    hikes = Hike.objects.all().order_by('name')
    hike_filter = HikeFilter(request.GET, queryset=hikes)
    hikes = hike_filter.qs
    context = {
        'hikes': hikes,
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
    species = Species.objects.all().order_by('scientific_name')
    species_filter = CerescopeFilter(request.GET, queryset=species)
    species = species_filter.qs
    context = {
        'species': species,
        'species_filter': species_filter
    }
    return render(request, 'ceresia/cerescope.html', context)


def achievements(request):
    return render(request, 'ceresia/achievements.html')


def login(request):
    return render(request, 'ceresia/login.html')
