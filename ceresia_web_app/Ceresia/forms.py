from django import forms
from Ceresia.models import Hike

from django.db import models


class HistoryForm(forms.ModelForm):
    name = models.CharField(max_length=10000, blank=False, default='default')
    date = forms.DateField()

    class Meta:
        model = Hike
        fields = [
            "name",
            "date"
        ]


class HistoryDeleteForm(forms.Form):
    delete = forms.HiddenInput()
