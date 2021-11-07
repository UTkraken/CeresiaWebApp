import os
from django.urls import path

from . import views

app_name = 'ceresia'

urlpatterns = [
    path('', views.home, name='home'),
]