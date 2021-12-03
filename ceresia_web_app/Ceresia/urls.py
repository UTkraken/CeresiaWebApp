import os
from django.urls import path

from . import views

app_name = 'Ceresia'

urlpatterns = [
    path('load-data', views.load, name="load"),
    path('', views.hikes, name='hikes'),
    path('parcours', views.hikes, name='hikes'),
    path('historique', views.history, name='history'),
    path('cerescope', views.cerescope, name='cerescope'),
    path('succes', views.achievements, name='achievements'),
    path('create_history', views.create_history, name='create_history'),
    path('delete_history', views.delete_history, name='delete_history'),
    path('delete_all_history', views.delete_all_history, name='delete_all_history'),
    path('login', views.login, name='login'),
]