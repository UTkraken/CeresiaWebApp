import os
from django.urls import path

from . import views

app_name = 'Ceresia'

urlpatterns = [
    path('', views.hikes, name='home'),
    path('parcours', views.hikes, name='hikes'),
    path('historique', views.history, name='history'),
    path('cerescope', views.cerescope, name='cerescope'),
    path('succes', views.achievements, name='achievements'),
    path('create_history', views.history, name='create_history'),
    path('login', views.login, name='login'),
]