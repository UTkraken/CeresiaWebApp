from django.forms import modelformset_factory
from django.shortcuts import render

from Ceresia.models import Hike, History, Species
from .filters import HikeFilter, CerescopeFilter, CountyFilter
from .forms import HistoryForm

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
    county_filter = CountyFilter(request.GET, queryset=hikes)
    hikes = county_filter.qs
    context = {
        'hikes': hikes,
        'hike_filter': hike_filter,
        'county_filter': county_filter
    }

    return render(request, 'ceresia/hikes.html', context)


def history(request):
    # HistoryFormSet = modelformset_factory(Hike, fields=('name',))
    form = HistoryForm(request.POST or None)

    history = History.objects.all()
    context = {
        'history': history,
        'form': form
    }

    return render(request, 'ceresia/history.html', context)


def create_history(request):
    # form to input a new student
    form = HistoryForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form
    }

    return render(request, "ceresia/history.html", context)


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
