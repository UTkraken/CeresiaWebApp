from django.db import models
from django_bleach.models import BleachField


class SerialNumber(models.Model):
    serial_number = BleachField(null=False)

    def str(self):
        return ''.join(self.serial_number)


class User(models.Model):
    lastname = BleachField(max_length=50, null=False)
    firstname = BleachField(max_length=50, null=False)
    email = BleachField(max_length=100, null=False)
    password = BleachField(max_length=50, null=False)
    serial_number = models.ForeignKey(SerialNumber, null=False, on_delete=models.CASCADE)

    def str(self):
        return ''.join(self.lastname, self.firstname, self.email, self.password, self.serial_number)


class Species(models.Model):
    family = BleachField(max_length=150, null=False)
    scientific_name = BleachField(max_length=150, null=False)
    weight = BleachField(max_length=150, null=False)
    height = BleachField(max_length=150, null=False)

    def str(self):
        return ''.join(self.family, self.scientific_name, self.weight, self.height)


class Hike(models.Model):
    num = models.AutoField
    name = BleachField(max_length=150, null=False)
    location = BleachField(max_length=150, null=False)
    rating = BleachField(max_length=150, null=True)
    county = BleachField(max_length=150, null=False)
    duration = BleachField(max_length=150, null=True, default="Null")
    distance = BleachField(max_length=150, null=True, default="Null")

    def str(self):
        return ''.join(self.name, self.location, self.rating, self.county, self.duration)


class Encounter(models.Model):
    serial_number = models.ForeignKey(SerialNumber, null=False, on_delete=models.CASCADE)
    scientific_name = models.ForeignKey(Species, null=False, on_delete=models.CASCADE)
    date = models.DateField()
    path = BleachField(null=False)

    def str(self):
        return ''.join(self.serial_number, self.scientific_name, self.date, self.path)


class History(models.Model):
    email = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    num_hike = models.ForeignKey(Hike, null=False, on_delete=models.CASCADE)
    date = models.DateField()

    def str(self):
        return ''.join(self.email, self.num_hike, self.date)
