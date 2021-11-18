import os
from django.urls import path

from . import views

app_name = 'ceresia'

urlpatterns = [
    path('parcours', views.hikes, name='hikes'),
    path('historique', views.history, name='history'),
    path('cerescope', views.cerescope, name='cerescope'),
]