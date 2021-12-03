from django.shortcuts import render, redirect

from .models import Hike, History, Species, User
from .filters import HikeFilter, CerescopeFilter, CountyFilter
from .forms import HistoryForm, HistoryDeleteForm

from . import fill_database


def load(request):
    fill_database.generate_data_docker()

    return redirect('/parcours')

def hikes(request):
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
    hike = Hike.objects.all()
    history = History.objects.all()
    context = {
        'history': history,
        'hikes': hike
    }

    return render(request, 'ceresia/history.html', context)


def create_history(request):
    form = HistoryForm(request.POST or None)

    historyFormName = request.POST['name']
    hike = Hike.objects.get(name=historyFormName)
    user = User.objects.get(email="thomas.burgard@ceresia.com")
    historyDate = request.POST['date']

    newHistory = History(num_hike=hike, date=historyDate, email=user)
    newHistory.save()

    hikeList = Hike.objects.all()
    historyList = History.objects.all()
    context = {
        "form": form,
        "hikes": hikeList,
        "history": historyList
    }
    return render(request, "ceresia/history.html", context)


def delete_history(request):
    form = HistoryDeleteForm(request.POST or None)
    if form.is_valid():
        if request.POST.get('delete') is not None:
            historyId = request.POST.get('delete')
            History.objects.filter(pk=historyId).delete()
        else:
            context = {
                "form": form,
            }

            return render(request, "ceresia/history.html", context)
    hikeList = Hike.objects.all()
    historyList = History.objects.all()
    context = {
        "form": form,
        "hikes": hikeList,
        "history": historyList
    }

    return render(request, "ceresia/history.html", context)


def delete_all_history(request):
    form = HistoryForm(request.POST or None)

    History.objects.all().delete()
    hike = Hike.objects.all()
    history = History.objects.all()
    context = {
        'history': history,
        'hikes': hike,
        'form': form
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
