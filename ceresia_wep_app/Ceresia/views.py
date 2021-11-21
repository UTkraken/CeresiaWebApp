from django.http import HttpResponse
from django.shortcuts import render


def hikes(request):
    return render(request, 'ceresia/hikes.html')


def history(request):
    return render(request, 'ceresia/history.html')


def cerescope(request):
    return render(request, 'ceresia/cerescope.html')


def achievements(request):
    return render(request, 'ceresia/achievements.html')


def login(request):
    return render(request, 'ceresia/login.html')
