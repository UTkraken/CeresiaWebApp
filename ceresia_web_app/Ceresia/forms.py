from django import forms
from Ceresia.models import Hike

from django.forms import ModelChoiceField


class HistoryForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Hike.objects.all().values_list('name', flat=True), initial=0)
    print(name)

    class Meta:
        model = Hike
        fields = [
            "name"
        ]
