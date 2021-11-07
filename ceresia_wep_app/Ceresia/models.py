from django.db import models
from django_bleach.models import BleachField


class SerialNumber(models.Model):
    serial_number = BleachField(null=False)


class User(models.Model):
    lastname = BleachField(max_length=50, null=False)
    firstname = BleachField(max_length=50, null=False)
    email = BleachField(max_length=100, null=False)
    password = BleachField(max_length=50, null=False)
    serial_number = models.ForeignKey(SerialNumber, null=False, on_delete=models.CASCADE)


class Species(models.Model):
    name = BleachField(max_length=150, null=False)
    family = BleachField(max_length=150, null=False)
    scientific_name = BleachField(max_length=150, null=False)
    weight = BleachField(max_length=150, null=False)
    height = BleachField(max_length=150, null=False)


class Hike(models.Model):
    num = models.AutoField
    name = BleachField(max_length=150, null=False)
    location = BleachField(max_length=150, null=False)
    rating = BleachField(max_length=150, null=False)
    county = BleachField(max_length=150, null=False)


class Encounter(models.Model):
    serial_number = models.ForeignKey(SerialNumber, null=False, on_delete=models.CASCADE)
    scientific_name = models.ForeignKey(Species, null=False, on_delete=models.CASCADE)
    date = models.DateField
    path = BleachField(null=False)


class History(models.Model):
    email = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    num_hike = models.ForeignKey(Hike, null=False, on_delete=models.CASCADE)
    date = models.DateField
